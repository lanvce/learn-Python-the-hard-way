cars=100#车辆总数
space_in_a_car=4.0#每辆车的座位
drivers=30#司机数量
passengers=90#乘客数量
car_not_driven=cars-drivers#空闲车数量
car_driven=drivers#使用的车数量
carpool_capacity=space_in_a_car*car_driven#使用的所有车座位总数
average_passenges_per_car=passengers/car_driven#每辆车平均载客量


print("There are cars",cars,"cars available.")
print("There are only ",drivers,"drivers available.")
print("There will be ",car_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have ",passengers,"people to carpool today.")
print("We need put about",average_passenges_per_car,"in each car.")
