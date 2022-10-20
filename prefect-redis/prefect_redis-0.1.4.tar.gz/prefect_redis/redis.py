"""Redis tasks"""
from typing import TYPE_CHECKING, Any, Optional

import cloudpickle
from prefect import task

if TYPE_CHECKING:
    from .credentials import RedisCredentials


@task
async def redis_set(
    credentials: "RedisCredentials",
    key: str,
    value: Any,
    ex: Optional[float] = None,
    px: Optional[float] = None,
    nx: bool = False,
    xx: bool = False,
) -> None:
    """Set a Redis key to a any value. Will use cloudpickle to convert `value` to
    binary representation.

    Args:
        credentials: Redis credential block
        key: Key to be set
        value: Value to be set to `key`. Does not accept open connections such as
            database-connections
        ex: If provided, sets an expire flag in seconds on `key` set
        px: If provided, sets an expire flag in milliseconds on `key` set
        nx: If set to `True`, set the value at `key` to `value` only if it does not
            already exist
        xx: If set tot `True`, set the value at `key` to `value` only if it already
            exists
    """
    return await redis_set_binary.fn(
        credentials, key, cloudpickle.dumps(value), ex, px, nx, xx
    )


@task
async def redis_set_binary(
    credentials: "RedisCredentials",
    key: str,
    value: bytes,
    ex: Optional[float] = None,
    px: Optional[float] = None,
    nx: bool = False,
    xx: bool = False,
) -> None:
    """Set a Redis key to a binary value

    Args:
        credentials: Redis credential block
        key: Key to be set
        value: Value to be set to `key`. Must be bytes
        ex: If provided, sets an expire flag in seconds on `key` set
        px: If provided, sets an expire flag in milliseconds on `key` set
        nx: If set to `True`, set the value at `key` to `value` only if it does not
            already exist
        xx: If set tot `True`, set the value at `key` to `value` only if it already
            exists
    """
    client = credentials.get_client()

    await client.set(key, value, ex=ex, px=px, nx=nx, xx=xx)
    await client.close()


@task
async def redis_get(
    credentials: "RedisCredentials",
    key: str,
) -> Any:
    """Get an object stored at a redis key. Will use cloudpickle to reconstruct
    the object.

    Args:
        credentials: Redis credential block
        key: Key to get

    Returns:
        Fully reconstructed object, decoded brom bytes in redis
    """
    binary_obj = await redis_get_binary.fn(credentials, key)

    return cloudpickle.loads(binary_obj)


@task
async def redis_get_binary(
    credentials: "RedisCredentials",
    key: str,
) -> bytes:
    """Get an bytes stored at a redis key

    Args:
        credentials: Redis credential block
        key: Key to get

    Returns:
        Bytes from `key` in Redis
    """
    client = credentials.get_client()

    ret = await client.get(key)

    await client.close()
    return ret


@task
async def redis_execute(
    credentials: "RedisCredentials",
    cmd: str,
) -> str:
    """Execute Redis command

    Args:
        credentials: Redis credential block
        cmd: Command to be executed

    Returns:
        Command response
    """
    client = credentials.get_client()

    ret = await client.execute_command(cmd)
    await client.close()

    return ret
