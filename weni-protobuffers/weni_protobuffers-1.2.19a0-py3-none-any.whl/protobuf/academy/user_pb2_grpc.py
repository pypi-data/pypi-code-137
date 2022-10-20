# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from weni.protobuf.academy import user_pb2 as weni_dot_protobuf_dot_academy_dot_user__pb2


class UserControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Update = channel.unary_unary(
                '/weni.academy.user.UserController/Update',
                request_serializer=weni_dot_protobuf_dot_academy_dot_user__pb2.UpdateUserLang.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_academy_dot_user__pb2.User.FromString,
                )


class UserControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=weni_dot_protobuf_dot_academy_dot_user__pb2.UpdateUserLang.FromString,
                    response_serializer=weni_dot_protobuf_dot_academy_dot_user__pb2.User.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'weni.academy.user.UserController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weni.academy.user.UserController/Update',
            weni_dot_protobuf_dot_academy_dot_user__pb2.UpdateUserLang.SerializeToString,
            weni_dot_protobuf_dot_academy_dot_user__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
