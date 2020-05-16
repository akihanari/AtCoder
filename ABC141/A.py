# coding: utf-8

weather = ['Sunny', 'Cloudy', 'Rainy']
S = input()
# print(S)

S_in = weather.index(S)
if S_in == 2:
    print(weather[0])
else:
    print(weather[S_in + 1])
