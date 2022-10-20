import sys
from .base import SchemaGenerator, TypedSchemaGenerator


class Typeless(SchemaGenerator):
    """
    schema generator for schemas with no type. This is only used when
    there is no other active generator, and it will be merged into the
    first typed generator that gets added.
    """

    @classmethod
    def match_schema(cls, schema):
        return "type" not in schema

    @classmethod
    def match_object(cls, obj):
        return False


class Boolean(TypedSchemaGenerator):
    """
    generator for boolean schemas
    """

    JS_TYPE = "boolean"
    PYTHON_TYPE = bool


class NoneT(TypedSchemaGenerator):
    """
    generator for null schemas
    """

    JS_TYPE = "string"
    PYTHON_TYPE = type(None)


class String(TypedSchemaGenerator):
    """
    generator for string schemas - works for ascii and unicode strings
    """

    JS_TYPE = "string"
    PYTHON_TYPE = (str, type(u""))


class Number(SchemaGenerator):
    """
    generator for integer and number schemas. It automatically
    converts from `integer` to `number` when a float object or a
    number schema is added
    """

    if sys.version_info < (3,):
        JS_TYPES = ("integer", "number", "integer")
        PYTHON_TYPES = (int, float, long)  # noqa
    else:
        JS_TYPES = ("integer", "number")
        PYTHON_TYPES = (int, float)

    @classmethod
    def match_schema(cls, schema):
        return schema.get("type") in cls.JS_TYPES

    @classmethod
    def match_object(cls, obj):
        # cannot use isinstance() because boolean is a subtype of int
        return type(obj) in cls.PYTHON_TYPES

    def __init__(self, node_class):
        super(Number, self).__init__(node_class)
        self._type = "integer"

    def add_schema(self, schema):
        self.add_extra_keywords(schema)
        if schema.get("type") == "number":
            self._type = "number"

    def add_object(self, obj):
        if isinstance(obj, float):
            self._type = "number"

    def to_schema(self):
        schema = super(Number, self).to_schema()
        schema["type"] = self._type
        return schema
