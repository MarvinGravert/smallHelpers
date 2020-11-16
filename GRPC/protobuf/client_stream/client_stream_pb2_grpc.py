# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import client_stream_pb2 as client__stream__pb2


class SimpelComStub(object):
    """package unary;

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NumberTrade = channel.unary_unary(
                '/SimpelCom/NumberTrade',
                request_serializer=client__stream__pb2.SimpleCall.SerializeToString,
                response_deserializer=client__stream__pb2.SimpleResponse.FromString,
                )


class SimpelComServicer(object):
    """package unary;

    """

    def NumberTrade(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimpelComServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NumberTrade': grpc.unary_unary_rpc_method_handler(
                    servicer.NumberTrade,
                    request_deserializer=client__stream__pb2.SimpleCall.FromString,
                    response_serializer=client__stream__pb2.SimpleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SimpelCom', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SimpelCom(object):
    """package unary;

    """

    @staticmethod
    def NumberTrade(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpelCom/NumberTrade',
            client__stream__pb2.SimpleCall.SerializeToString,
            client__stream__pb2.SimpleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
