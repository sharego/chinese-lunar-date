#!/usr/bin/python
# encoding: utf-8
'''
Just like solar calendar , there is leap year,
which means the february has one more day than normal year.
In Lunar calendar , there is also leap year,
which means there are 13 months while normal year have 12 .  

Use Examples:
    I. scope:
        START_LUNAR, START_SOLAR, END_LUNAR, END_SOLAR
        contains_lunar(lunar)
        contains_solar(solar)

    II. switch solar with lunar
        lunar = LunarDate(2013,10,27)
        lunar = LunarDate.fromsolar(date(1900,1,1))
        lunar.tosolar()

    III. make lunar data
        make_data_of_year(normalmonthtypes,leapmonth=0,leaptype=0)

    IV. check lunar data
        show_year_info(year=None)
        
Declare:
    these data come from internet(Thanks a lot):
        http://www.ahszjt.gov.cn/Cal.htm (as standard)
        http://rili.tee5.com/
        http://www.guojiele.com/cal-0-0.html

    Although I check them very carefully, but maybe still have some wrong data
    If you find, welcome to tell me, Thanks

@author: xiaowei xw.cht.y@gmail.com
'''

from __future__ import print_function
from datetime import date,datetime,timedelta
from functools import total_ordering

###############
# Calendar data
###############


LUNAR_DATA_START_YEAE = 1899 # start lunar
LUNAR_DATA_STAER_SOLAE = date(1899,2,10) # start solar

LUNAR_DATA = [                 0x0ab50, 0x04bd8,    # 1899 - 1900
    0x04ae0, 0x0a570, 0x054d5, 0x0d260, 0x0d950,    # 1905 
    0x16554, 0x056a0, 0x09ad0, 0x055d2, 0x04ae0,    # 1910 
    0x0a5b6, 0x0a4d0, 0x0d250, 0x1d255, 0x0b540,    # 1915 
    0x0d6a0, 0x0ada2, 0x095b0, 0x14977, 0x04970,    # 1920 
    0x0a4b0, 0x0b4b5, 0x06a50, 0x06d40, 0x1ab54,    # 1925 
    0x02b60, 0x09570, 0x052f2, 0x04970, 0x06566,    # 1930 
    0x0d4a0, 0x0ea50, 0x16a95, 0x05ad0, 0x02b60,    # 1935 
    0x186e3, 0x092e0, 0x1c8d7, 0x0c950, 0x0d4a0,    # 1940 
    0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, 0x025d0,    # 1945 
    0x092d0, 0x0d2b2, 0x0a950, 0x0b557, 0x06ca0,    # 1950 
    0x0b550, 0x15355, 0x04da0, 0x0a5b0, 0x14573,    # 1955 
    0x052b0, 0x0a9a8, 0x0e950, 0x06aa0, 0x0aea6,    # 1960 
    0x0ab50, 0x04b60, 0x0aae4, 0x0a570, 0x05260,    # 1965 
    0x0f263, 0x0d950, 0x05b57, 0x056a0, 0x096d0,    # 1970 
    0x04dd5, 0x04ad0, 0x0a4d0, 0x0d4d4, 0x0d250,    # 1975 
    0x0d558, 0x0b540, 0x0b6a0, 0x195a6, 0x095b0,    # 1980 
    0x049b0, 0x0a974, 0x0a4b0, 0x0b27a, 0x06a50,    # 1985 
    0x06d40, 0x0af46, 0x0ab60, 0x09570, 0x04af5,    # 1990 
    0x04970, 0x064b0, 0x074a3, 0x0ea50, 0x06b58,    # 1995 
    0x05ac0, 0x0ab60, 0x096d5, 0x092e0, 0x0c960,    # 2000 
    0x0d954, 0x0d4a0, 0x0da50, 0x07552, 0x056a0,    # 2005 
    0x0abb7, 0x025d0, 0x092d0, 0x0cab5, 0x0a950,    # 2010 
    0x0b4a0, 0x0baa4, 0x0ad50, 0x055d9, 0x04ba0,    # 2015 
    0x0a5b0, 0x15176, 0x052b0, 0x0a930, 0x07954,    # 2020 
    0x06aa0, 0x0ad50, 0x05b52, 0x04b60, 0x0a6e6,    # 2025 
    0x0a4e0, 0x0d260, 0x0ea65, 0x0d530, 0x05aa0,    # 2030 
    0x076a3, 0x096d0, 0x04afb, 0x04ad0, 0x0a4d0,    # 2035 
    0x1d0b6, 0x0d250, 0x0d520, 0x0dd45, 0x0b5a0,    # 2040 
    0x056d0, 0x055b2, 0x049b0, 0x0a577, 0x0a4b0,    # 2045 
    0x0aa50, 0x1b255, 0x06d20, 0x0ada0, 0x14b63,    # 2050 
    0x09370, 0x049f8, 0x04970, 0x064b0, 0x168a6,    # 2055
    0x0ea50, 0x06aa0, 0x1a6c4, 0x0aae0, 0x092e0,    # 2060
    0x0d2e3, 0x0c960, 0x0d557, 0x0d4a0, 0x0da50,    # 2065
    0x05d55, 0x056a0, 0x0a6d0, 0x055d4, 0x052d0,    # 2070
    0x0a9b8, 0x0a950, 0x0b4a0, 0x0b6a6, 0x0ad50,    # 2075
    0x055a0, 0x0aba4, 0x0a5b0, 0x052b0, 0x0b273,    # 2080
    0x06930, 0x07337, 0x06aa0, 0x0ad50, 0x14b55,    # 2085
    0x04b60, 0x0a570, 0x054e4, 0x0d160, 0x0e968,    # 2090
    0x0d520, 0x0daa0, 0x16aa6, 0x056d0, 0x04ae0,    # 2095
    0x0a9d4, 0x0a2d0, 0x0d150, 0x0f252, 0x0d520,    # 2100
]

def make_data_of_year(normalmonth,leapmonth=0,leaptype=0):
    ''' generate a year lunar data like 0x0aa50
    @param normalmonth: sequence(bool), the normal 12 months type
        if it is a big month then there are 30 days
        else it is a small month , there are 29 days
    @param leapmonth: int, the leap month. 0 means no leap month
    @param leaptype: bool, the leap month type (big or small)
    
    data format: b bbbb bbbb bbbb bbbb ( this format is from internet )
           first bit : the leap month type , big or small
           then 12 bits: each months type, big or small
           last 4 bits : the leap month , 0 means no leap month
    big month has 30 days , small month has 29 days
    '''
    assert isinstance(normalmonth,(str,tuple,list) ) and \
        len(normalmonth) == 12 , 'months data error'
    assert isinstance(leapmonth,int) and 0 <= leapmonth < 13 , 'month error'
    normalmonth = ''.join('1' if x else '0' for x in normalmonth )
    v = int(normalmonth,2) << 4
    v += leapmonth + ( 0x10000 if leaptype else 0 )
    return '0x%05x' % (v,)

def parse_data_leap( v ):
    ''' parse the lunar data of one year to get leap info
    return leap month and days of this leap month
    '''
    return v&0xf , bool( v&0xf ) * (29 + bool(v & 0x10000))

def parse_data_days( v ):
    '''parse data which generates by make_data_of_year function
        return a list contains leap month days, each month days , leap month
    '''
    leap_moth , leap_days = parse_data_leap( v )
    month = (v & 0xfff0 ) >> 4 
    r = [ leap_days ]
    r.extend( 29 + bool( month & (1<<i))  for i in range(11,-1,-1) )
    r.append( leap_moth )
    return r

def parse_year(year):
    return parse_data_days( LUNAR_DATA[ year - LUNAR_DATA_START_YEAE ] )

def year_leap(year):
    'None if no leap month of the year or leap month and days'
    return parse_data_leap( LUNAR_DATA[ year - LUNAR_DATA_START_YEAE ] )

def days_of_month(year,month):
    '''return days of the special month in Lunar Calendar
        there two values if the month is leap
    '''
    info = parse_year(year)
    ret = [info[month]]
    if info[-1] == month: # is leap month
        ret.append(info[0])
    return ret

def month_days_of_year(year):
    year_days = parse_year(year)
    days_of_months = year_days[1:-1] # the normal month days
    if year_days[-1]: # leap month: normal month before, leap month later
        days_of_months.insert( year_days[-1], year_days[0]  )
    return days_of_months

def lastdate_of_year(year):
    v = LUNAR_DATA[ year - START_LUNAR.year ]
    return BasicLunarDate( year, 12, 30 if v & 0x10 else 29,
                      1 if v & 0xff == 12 else 0  )
    
def lastdate_of_month(year,month):
    days = days_of_month(year,month)
    return BasicLunarDate( year, month , days[-1], len(days) == 2 )

###############
# Calendar info
###############

###############
# Basic Lunar Date
###############

LUNAR_NAME = '农历'
YEAR = '年'
MONTH = '月'
DAY = '日'
DAYS = '天'
LEAP  = '闰'
MONTH_NAMES = '正二三四五六七八九十冬腊'
MONTH_TYPES = '小大'
NUMBERS = '一二三四五六七八九十'
TEN_DAYS = '初十廿三'
ANIMALS = "鼠牛虎兔龙蛇马羊猴鸡狗猪"

def format_year(n):
    return str(n)+YEAR

def format_month(n,leap=0):
    return (LEAP if leap else '') + MONTH_NAMES[n-1] + MONTH

def format_day(n):
    if n == 10:
        return TEN_DAYS[:2]
    elif n % 10 == 0:
        return NUMBERS[n//10] + NUMBERS[-1]
    return TEN_DAYS[n//10] + NUMBERS[n%10-1] + DAY

def show_year_info(year=None):
    'show lunar year data info, to help check LUNAR_DATA right'
    def year_info(i):
        v = LUNAR_DATA[i]
        year = i + LUNAR_DATA_START_YEAE
        days = DAYS_OF_YEAR[year]
        animal = ANIMALS[(year - 1900 ) % 12]
        s =  '%s%s%s(%s) %d%s: ' % (LUNAR_NAME, year, YEAR, animal, days , DAYS )
        months = []
        for i in range(12):
            name = MONTH_NAMES[i]
            mtype = MONTH_TYPES[ bool( v & ( 0x8000 >> i) ) ]
            months.append( '%s%s(%s)' % (name , MONTH, mtype ) )
        assert isinstance(v,int), v
        if v & 0x0f:
            name = MONTH_NAMES[(v&0xf)-1]
            mtype = MONTH_TYPES[ bool( v&0x10000) ]
            months.insert(v&0xf, '%s%s%s(%s)' % (LEAP, name, MONTH, mtype) )
        return s + ', '.join(months)
    if not year:
        for x in range(len(LUNAR_DATA)):
            print(year_info(x))
    else:
        assert LUNAR_DATA_START_YEAE <= year <= LUNAR_DATA_END_YEAE
        print(year_info(year-LUNAR_DATA_START_YEAE))

@total_ordering
class BasicLunarDate(object):
    def __init__(self , year , month , day , leap = 0 ):
        if not all([isinstance(x,int) for x in (year,month,day)]):
            raise TypeError( '%s|%s|%s' % (year,month,day) )
        msg = 'wrong data: %4d-%2d-%2d' % (year,month,day)
        assert year>0 and 0<month<13 and 0<day<31 , msg
        self.year = year
        self.month = month
        self.day = day
        self.leap = bool(leap)
        
    def __eq__(self,oth):
        return repr(self) == repr(oth)
        
    def __lt__(self,oth):
#        assert isinstance(oth, self.__class__ ) , 'type error'
        sym = self.year * 100 + self.month
        oym =  oth.year * 100 +  oth.month
        if sym != oym:
            return sym < oym
        if self.leap != oth.leap:
            return not self.leap
        return self.day < oth.day
    
    def __str__(self):
        return LUNAR_NAME+''.join([format_year(self.year),
                    format_month(self.month,self.leap),
                    format_day(self.day) ] )
        
    def __repr__(self):
        return 'BasicLunarDate(%d,%d,%d,%d)' % tuple(self.data())
        
    def data(self):
        return [self.year,self.month,self.day,int(bool(self.leap))]


# Contants
LUNAR_DATA_END_YEAE = LUNAR_DATA_START_YEAE+len(LUNAR_DATA)-1

DAYS_OF_YEAR = {}

for i in range( len(LUNAR_DATA) ):
    year = LUNAR_DATA_START_YEAE + i
    days = sum( parse_data_days( LUNAR_DATA[i] )[:-1] )
    DAYS_OF_YEAR[year] = days

DAYS_OF_DATA = sum( DAYS_OF_YEAR[i] for i in DAYS_OF_YEAR )

START_LUNAR = BasicLunarDate(LUNAR_DATA_START_YEAE,1,1)
START_SOLAR = LUNAR_DATA_STAER_SOLAE
END_SOLAR   = START_SOLAR + timedelta(DAYS_OF_DATA-1)
END_LUNAR   = lastdate_of_year( LUNAR_DATA_END_YEAE )

def contains_solar(solar):
    'check this lunar calendar contains the solar date'
    d = solar if isinstance(solar,date) else solar.date()
    return START_SOLAR <= d <= END_SOLAR
    
def contains_lunar(lunar):
    'check this lunar calendar contains the lunar date'
    assert isinstance(lunar, BasicLunarDate) , 'type error'
    month = lunar.month
    if START_LUNAR <= lunar <= END_LUNAR and 0<month<13:
        mdays = days_of_month(lunar.year, month)
        if not lunar.leap or len(mdays) == 2:
            return 0<lunar.day <= ( mdays[1] if lunar.leap else mdays[0] )
    return False

contains = contains_lunar

def lunar_count_days(lunar):
    'return days from LUNAR_START to lunar'
    if not contains(lunar):
        raise IndexError
    days = 0
    for year in range(START_LUNAR.year,lunar.year):
        days += DAYS_OF_YEAR[year]
    days_of_months = month_days_of_year(lunar.year)
    end_index = lunar.month - 1
    leap_month, _ = year_leap(lunar.year)
    if leap_month:
       if lunar.month > leap_month or \
       ( lunar.month == leap_month and lunar.leap ):
           end_index = lunar.month
            
    days += sum(days_of_months[:end_index]) + lunar.day -1
    return days

def lunar_next(lunar):
    'return the next lunar date of lunar, normal month first, leap month late'
    if lunar >= END_LUNAR or lunar < START_LUNAR:
        raise IndexError
    year,month,day,leap = lunar.data()
    if month == 12 and day >= 29:
        if lunar == lastdate_of_year(year):
            leap_month, leap_days = year_leap(year+1)
            return BasicLunarDate( year+1,1,1,1==leap_month )
    leap_month, leap_days = year_leap(year)
    days = days_of_month(year, month)
    # check total days in this month
    if leap :
        assert leap_month == month , 'leap month error:'+str(lunar)
        month_days = days[1]
    else:
        month_days = days[0]
    
    m, d, l = month, day+1, leap

    if day == month_days:
        d = 1
        if leap_month == month and not leap:
            l = 1
        else:
            m = month+1
            l = 0
    return BasicLunarDate(year,m,d,l)
        
def lunartosolar(lunar):
    'switch lunar date to solar date'
    return START_SOLAR + timedelta( lunar_count_days(lunar) )

def solartolunar(solar):
    'switch solar date to lunar date'
    if not contains_solar(solar):
        raise IndexError(str(solar)+';'+str(START_SOLAR))
    days = ( solar - START_SOLAR ).days
    lunar_days = sum(DAYS_OF_YEAR[i] for i in range(LUNAR_DATA_START_YEAE,solar.year))
    cur_days = lunar_days
    year = solar.year
    if lunar_days > days:
        year = solar.year-1
        cur_days -= DAYS_OF_YEAR[solar.year-1]
    elif lunar_days + DAYS_OF_YEAR[solar.year] < days:
            year = solar.year + 1
            cur_days += DAYS_OF_YEAR[solar.year]
    elif lunar_days == days:
        return BasicLunarDate(solar.year, 1 , 1)
    
    days_of_months = month_days_of_year(year)
    leap_month, _ = year_leap(year)
    t = cur_days
    for i, v in enumerate(days_of_months):
        month = i + 1 if not leap_month or i < leap_month else i
        if t + v > days: # in this month
            return BasicLunarDate(year, month , days-t+1, leap_month and i == leap_month  )
        elif t+v == days: # the first day of next month
            leap = False
            if leap_month and i+1 == leap_month:
                leap = True
            else:
                month += 1
            return BasicLunarDate(year, month, 1 , leap )
        else:
            t += v
    raise Exception( 'solar[%s] to lunar[error]' % (solar,) )


###############
# Lunar Date
###############

class LunarDate(BasicLunarDate):
    
    def __init__(self,*args):
        'year, month, day, leap=0'
        if len(args) == 1:
            assert isinstance(args[0], BasicLunarDate)
            y,m,d,l = args[0].data()
        else:
            assert 3 <= len(args) <= 4
            y,m,d = args[:3]
            l = args[-1] if len(args) > 3 else 0

        BasicLunarDate.__init__(self,y,m,d,l)

        if not contains(self):
            raise Warning('not contain')
    
    @staticmethod
    def fromsolar(solar,m=None,d=None):
        if not isinstance(solar,(date,datetime)):
            t = date.today()
            if not m:
                m = t.month
            if not d:
                d = t.day
            solar = date(solar,m,d)
        return LunarDate( solartolunar(solar) )
    
    @staticmethod
    def today():
        return LunarDate.fromsolar( date.today() )
    
    def tosolar(self):
        return lunartosolar(self)
    
    def next(self):
        return lunar_next(self)
    
    def __add__(self, delta ):
        'x+y, timedelta'
        solar = self.tosolar() + delta
        return LunarDate.fromsolar(solar)
    
    def getanimal(self):
        '1900 is pig year'
        return ANIMALS[(self.year - 1900 ) % 12]

def traverse():
    oneday = timedelta(1)
    cur_solar = START_SOLAR
    while cur_solar < END_SOLAR:
        cur_lunar = solartolunar(cur_solar)
        yield cur_solar, cur_lunar
        cur_solar += oneday

def __test():
    cur_solar = START_SOLAR
    cur_lunar = START_LUNAR
    oneday = timedelta(1)
    pre_info = None
    while cur_lunar < END_LUNAR:
        
        lunar = solartolunar(cur_solar)
        solar = lunartosolar(cur_lunar)
        solar2 = lunartosolar(lunar) if cur_lunar != lunar else solar
        
        info_fmt = "           real solar[%s]\n" +\
                   "           real lunar[%s]\n" +\
                   "  real lunar to solar[%s]\n" +\
                   "  real solar to lunar[%s]\n" +\
                   "  real lunar to  next[%s]"
        
        cur_info = cur_solar, cur_lunar, solar, lunar,  lunar_next( cur_lunar )
        
        check = cur_solar == solar and solar == solar2 and cur_lunar == lunar
        
        if not check:
            if pre_info:
                print(info_fmt % pre_info)
                print('---')
            print(info_fmt % cur_info)
            assert 0

        cur_solar += oneday
        cur_lunar = lunar_next( cur_lunar )
        pre_info  = cur_info


if __name__ == '__main__':
#    print( make_data_of_year([0,1,0,0,5,0,7,8,0,10,11,0],3,1) )
    __test()

    print( lunartosolar(LunarDate(1970,1,1)))
    print( END_SOLAR)
    print( 'Test End.' )

