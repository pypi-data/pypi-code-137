# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from weni.protobuf.connect import organization_pb2 as weni_dot_protobuf_dot_connect_dot_organization__pb2


class OrganizationControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/weni.connect.project.OrganizationController/List',
                request_serializer=weni_dot_protobuf_dot_connect_dot_organization__pb2.OrganizationListRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_connect_dot_organization__pb2.OrganizationResponse.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/weni.connect.project.OrganizationController/Retrieve',
                request_serializer=weni_dot_protobuf_dot_connect_dot_organization__pb2.OrganizationRetrieveRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_connect_dot_organization__pb2.OrganizationResponse.FromString,
                )


class OrganizationControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrganizationControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=weni_dot_protobuf_dot_connect_dot_organization__pb2.OrganizationListRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_connect_dot_organization__pb2.OrganizationResponse.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=weni_dot_protobuf_dot_connect_dot_organization__pb2.OrganizationRetrieveRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_connect_dot_organization__pb2.OrganizationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'weni.connect.project.OrganizationController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrganizationController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/weni.connect.project.OrganizationController/List',
            weni_dot_protobuf_dot_connect_dot_organization__pb2.OrganizationListRequest.SerializeToString,
            weni_dot_protobuf_dot_connect_dot_organization__pb2.OrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weni.connect.project.OrganizationController/Retrieve',
            weni_dot_protobuf_dot_connect_dot_organization__pb2.OrganizationRetrieveRequest.SerializeToString,
            weni_dot_protobuf_dot_connect_dot_organization__pb2.OrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
