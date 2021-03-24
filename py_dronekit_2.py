from dronekit import connect, Vehicle
from my_vehicle import MyVehicle #Our custom vehicle class
from pymavlink import mavutil
import time, sys, argparse, math

print("connecting")

connection_string = '/dev/ttyACM0'
vehicle = connect(connection_string, wait_ready=True,vehicle_class=MyVehicle)

def raw_imu_callback(self, attr_name, value):
    # attr_name == 'raw_imu'
    # value == vehicle.raw_imu
    print(value)
while True:
    vehicle.add_attribute_listener('raw_imu', raw_imu_callback)
    
    time.sleep(1)

