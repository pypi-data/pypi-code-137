# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from weni.protobuf.flows import billing_pb2 as weni_dot_protobuf_dot_flows_dot_billing__pb2


class BillingControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Total = channel.unary_unary(
                '/weni.flows.billing.BillingController/Total',
                request_serializer=weni_dot_protobuf_dot_flows_dot_billing__pb2.BillingRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_flows_dot_billing__pb2.TotalResponse.FromString,
                )
        self.Detailed = channel.unary_stream(
                '/weni.flows.billing.BillingController/Detailed',
                request_serializer=weni_dot_protobuf_dot_flows_dot_billing__pb2.BillingRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_flows_dot_billing__pb2.ActiveContactDetail.FromString,
                )
        self.MessageDetail = channel.unary_unary(
                '/weni.flows.billing.BillingController/MessageDetail',
                request_serializer=weni_dot_protobuf_dot_flows_dot_billing__pb2.MessageDetailRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_flows_dot_billing__pb2.MsgDetail.FromString,
                )


class BillingControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Total(self, request, context):
        """Get the total or active contacts in a time range
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Detailed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MessageDetail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BillingControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Total': grpc.unary_unary_rpc_method_handler(
                    servicer.Total,
                    request_deserializer=weni_dot_protobuf_dot_flows_dot_billing__pb2.BillingRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_flows_dot_billing__pb2.TotalResponse.SerializeToString,
            ),
            'Detailed': grpc.unary_stream_rpc_method_handler(
                    servicer.Detailed,
                    request_deserializer=weni_dot_protobuf_dot_flows_dot_billing__pb2.BillingRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_flows_dot_billing__pb2.ActiveContactDetail.SerializeToString,
            ),
            'MessageDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.MessageDetail,
                    request_deserializer=weni_dot_protobuf_dot_flows_dot_billing__pb2.MessageDetailRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_flows_dot_billing__pb2.MsgDetail.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'weni.flows.billing.BillingController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BillingController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Total(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weni.flows.billing.BillingController/Total',
            weni_dot_protobuf_dot_flows_dot_billing__pb2.BillingRequest.SerializeToString,
            weni_dot_protobuf_dot_flows_dot_billing__pb2.TotalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Detailed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/weni.flows.billing.BillingController/Detailed',
            weni_dot_protobuf_dot_flows_dot_billing__pb2.BillingRequest.SerializeToString,
            weni_dot_protobuf_dot_flows_dot_billing__pb2.ActiveContactDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MessageDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weni.flows.billing.BillingController/MessageDetail',
            weni_dot_protobuf_dot_flows_dot_billing__pb2.MessageDetailRequest.SerializeToString,
            weni_dot_protobuf_dot_flows_dot_billing__pb2.MsgDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
