import math


def gen_rough_resolution(width, height):
    origin_text = '''weapon1 = "3043,2081"
weapon2 = "3645,2078"
r99 = "3167,1955,1,3298,1961,0,3389,1964,1"
r301 = "3154,1940,1,3314,1955,0,3385,1956,1"
re45 = "3212,1950,1,3280,1962,0,3324,2009,1"
p2020 = "3209,1939,1,3264,1964,0,3303,2010,1"
g7 = "3146,1950,1,3318,1962,0,3406,1980,1"
flatline = "3140,1951,1,3269,1960,0,3330,1987,1"
prowler = "3219,1981,1,3271,1969,0,3346,1953,1"
hemlok = "3213,1967,1,3296,1971,0,3377,1972,1"
rampage = "3119,1952,1,3292,1968,0,3403,1966,1"
wingman = "3205,1969,1,3290,1970,0,3316,2002,1"
lstar = "3159,1989,1,3281,1980,0,3334,1938,1"
devotion = "3400,1942,1,3324,1960,0,3122,1944,1"
volt = "3288,1962,0,3170,1952,1,3360,1942,1"
havoc = "3312,1992,1,3316,1970,0,3274,1924,1"
spitfire = "3386,1944,1,3304,1978,1,3290,1924,1"
alternator = "3230,1958,1,3284,1960,1,3292,1956,0"
car = "3210,1940,1,3172,1946,1,3210,1942,1"
havoc_turbocharger = "3242,2012"
devotion_turbocharger = "3300,2014"'''
    print('[pixels]')
    lines = origin_text.split("\n")
    for line in lines:
        t1 = line.split(" = ")
        res = t1[0] + ' = "'
        t2 = t1[1][1: -1].split(",")
        for i in range(len(t2)):
            if i % 3 == 0:
                res += str(math.floor(int(t2[i]) * width / 3840))
            elif i % 3 == 1:
                res += str(math.floor(int(t2[i]) * height / 2160))
            else:
                res += t2[i]
            if i != len(t2) - 1:
                res += ','
        res += '"'
        print(res)


if __name__ == '__main__':
    print("Width: ", end='')
    width = input()
    print("Height: ", end='')
    height = input()
    gen_rough_resolution(int(width), int(height))

