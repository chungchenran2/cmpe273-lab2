from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc

def run():
	with grpc.insecure_channel('localhost:50051') as channel:
		stub = calculator_pb2_grpc.CalculatorStub(channel)
		response = stub.add(calculator_pb2.OperandsRequest(value1=3,value2=5))
	print("The result of 3 + 5 is " + response.message)

if __name__ == '__main__':
	run()