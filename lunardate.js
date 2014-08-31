/* UTF8
 * chinese lunar conversion
 * author: xiaowei (xw.cht.y@gmail.com)
 *
 *
 * usage:
 *
 *       lunar = LunarCalendar.LunarDate.fromsolar()
 *       lunar = new LunarCalendar.LunarDate(year,month,day,leap)
 *       solar = lunar.tosolar()
 */

(function(define,E){

    if(!define){
        define = function(f){
            E.LunarCalendar = f() // export
        }
    }

    define(function(){
        var TIMEZONE_OFFSET = new Date().getTimezoneOffset() // for UTC
        var LUNAR_DATE_CONSTANT = {
            "LUNAR_DATA_START_YEAE": 1899 // start lunar 1899-1-1
            // start solar: Feb 10, 1899
            ,"LUNAR_DATA_STAER_SOLAE": new Date(1899,2-1,10,TIMEZONE_OFFSET/-60) 
            ,"LUNAR_DATA" : [              0x0ab50, 0x04bd8,    // 1899 - 1900
                0x04ae0, 0x0a570, 0x054d5, 0x0d260, 0x0d950,    // 1905 
                0x16554, 0x056a0, 0x09ad0, 0x055d2, 0x04ae0,    // 1910 
                0x0a5b6, 0x0a4d0, 0x0d250, 0x1d255, 0x0b540,    // 1915 
                0x0d6a0, 0x0ada2, 0x095b0, 0x14977, 0x04970,    // 1920 
                0x0a4b0, 0x0b4b5, 0x06a50, 0x06d40, 0x1ab54,    // 1925 
                0x02b60, 0x09570, 0x052f2, 0x04970, 0x06566,    // 1930 
                0x0d4a0, 0x0ea50, 0x16a95, 0x05ad0, 0x02b60,    // 1935 
                0x186e3, 0x092e0, 0x1c8d7, 0x0c950, 0x0d4a0,    // 1940 
                0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, 0x025d0,    // 1945 
                0x092d0, 0x0d2b2, 0x0a950, 0x0b557, 0x06ca0,    // 1950 
                0x0b550, 0x15355, 0x04da0, 0x0a5b0, 0x14573,    // 1955 
                0x052b0, 0x0a9a8, 0x0e950, 0x06aa0, 0x0aea6,    // 1960 
                0x0ab50, 0x04b60, 0x0aae4, 0x0a570, 0x05260,    // 1965 
                0x0f263, 0x0d950, 0x05b57, 0x056a0, 0x096d0,    // 1970 
                0x04dd5, 0x04ad0, 0x0a4d0, 0x0d4d4, 0x0d250,    // 1975 
                0x0d558, 0x0b540, 0x0b6a0, 0x195a6, 0x095b0,    // 1980 
                0x049b0, 0x0a974, 0x0a4b0, 0x0b27a, 0x06a50,    // 1985 
                0x06d40, 0x0af46, 0x0ab60, 0x09570, 0x04af5,    // 1990 
                0x04970, 0x064b0, 0x074a3, 0x0ea50, 0x06b58,    // 1995 
                0x05ac0, 0x0ab60, 0x096d5, 0x092e0, 0x0c960,    // 2000 
                0x0d954, 0x0d4a0, 0x0da50, 0x07552, 0x056a0,    // 2005 
                0x0abb7, 0x025d0, 0x092d0, 0x0cab5, 0x0a950,    // 2010 
                0x0b4a0, 0x0baa4, 0x0ad50, 0x055d9, 0x04ba0,    // 2015 
                0x0a5b0, 0x15176, 0x052b0, 0x0a930, 0x07954,    // 2020 
                0x06aa0, 0x0ad50, 0x05b52, 0x04b60, 0x0a6e6,    // 2025 
                0x0a4e0, 0x0d260, 0x0ea65, 0x0d530, 0x05aa0,    // 2030 
                0x076a3, 0x096d0, 0x04afb, 0x04ad0, 0x0a4d0,    // 2035 
                0x1d0b6, 0x0d250, 0x0d520, 0x0dd45, 0x0b5a0,    // 2040 
                0x056d0, 0x055b2, 0x049b0, 0x0a577, 0x0a4b0,    // 2045 
                0x0aa50, 0x1b255, 0x06d20, 0x0ada0, 0x14b63,    // 2050 
                0x09370, 0x049f8, 0x04970, 0x064b0, 0x168a6,    // 2055
                0x0ea50, 0x06aa0, 0x1a6c4, 0x0aae0, 0x092e0,    // 2060
                0x0d2e3, 0x0c960, 0x0d557, 0x0d4a0, 0x0da50,    // 2065
                0x05d55, 0x056a0, 0x0a6d0, 0x055d4, 0x052d0,    // 2070
                0x0a9b8, 0x0a950, 0x0b4a0, 0x0b6a6, 0x0ad50,    // 2075
                0x055a0, 0x0aba4, 0x0a5b0, 0x052b0, 0x0b273,    // 2080
                0x06930, 0x07337, 0x06aa0, 0x0ad50, 0x14b55,    // 2085
                0x04b60, 0x0a570, 0x054e4, 0x0d160, 0x0e968,    // 2090
                0x0d520, 0x0daa0, 0x16aa6, 0x056d0, 0x04ae0,    // 2095
                0x0a9d4, 0x0a2d0, 0x0d150, 0x0f252, 0x0d520,    // 2100
            ]
            ,"LUNAR_NAME":"农历"
            ,"YEAR":"年"
            ,"MONTH":"月"
            ,"DAY":"日"
            ,"DAYS":"天"
            ,"LEAP":"闰"
            ,"MONTH_NAMES":"正二三四五六七八九十冬腊"
            ,"MONTH_TYPES":"小大"
            ,"NUMBERS":"一二三四五六七八九十"
            ,"TEN_DAYS":"初十廿三"
            ,"ANIMALS":"鼠牛虎兔龙蛇马羊猴鸡狗猪"
            // calculate
            ,"LUNAR_DATA_END_YEAE" : 0
        };

        var exports = {"cache_limits":1000} // 0 means no cache


        var LunarDate = function(y,m,d,l){
            this.year = y || -1;
            this.month = m || 1;
            this.day = d || 1;
            this.leap = l || 0;
        };

        LunarDate.prototype.toDataString = function() {
            return [this.year,this.month,this.day,
                Boolean(this.leap)?1:0 ].join('-')
        };

        LunarDate.prototype.toString = function(){
            var C = LUNAR_DATE_CONSTANT,day = this.day,d

            if( day == 10){
                d = C.TEN_DAYS.slice(0,2)
            } else if( day % 10 == 0 ){
                d = C.NUMBERS[ parseInt(day/10) -1 ] + C.NUMBERS[9]
            } else {
                d = C.TEN_DAYS[parseInt(day/10)] + C.NUMBERS[day%10-1]
            }

            return [this.year,C.YEAR
                    ,this.leap?C.LEAP:''
                    ,C.MONTH_NAMES[this.month-1],C.MONTH
                    ,d].join('')
        };

        var LunarFunction = {
            "parse":{
                "data":{
                    "init":function(){ // calculate other constant
                        if( "DAYS_OF_YEAR" in LUNAR_DATE_CONSTANT ){ // executed
                            return
                        }
                        var C = LUNAR_DATE_CONSTANT,o=this
                        C.LUNAR_DATA_END_YEAE = C.LUNAR_DATA_START_YEAE+C.LUNAR_DATA.length-1
                        var r = {},t = 0, D = C.LUNAR_DATA
                        D.forEach(function(v,i){
                            var y = C.LUNAR_DATA_START_YEAE + i,
                                day = o.month_days(D[i]).slice(0,-1),
                                d = day.reduce(function(b,v){return b+v},0) // sum
                            r[y] = d
                            t += d
                        })
                        C.DAYS_OF_YEAR = r
                        C.DAYS_OF_DATA = t
                    },
                    "leap":function(v){ // parse leap data
                        return [v&0xf, Boolean( v&0xf ) * (29 + Boolean(v & 0x10000))]
                    },
                    "month_days":function(v){ // parse month data ret.length=14
                        var leapinfo = this.leap(v),
                             leap_month = leapinfo[0], leap_days = leapinfo[1],
                        normalmonth = (v & 0xfff0 ) >> 4 ,
                        r = [ leap_days ];
                        for(var i=11;i>-1;i--){
                            r.push( 29 + Boolean( normalmonth & (1<<i)) )
                        }
                        r.push( leap_month )
                        return r
                    },
                    "get_year":function(year){ // get special year lunar data
                        var C = LUNAR_DATE_CONSTANT
                        return C.LUNAR_DATA[ year - C.LUNAR_DATA_START_YEAE ]
                    },
                    "get_last_year":function(){
                        var C = LUNAR_DATE_CONSTANT
                        return C.LUNAR_DATA.length + C.LUNAR_DATA_START_YEAE
                    }
                },
                "year":function(year){ // parse this year data
                    return this.data.month_days( this.data.get_year(year) )
                },
                "year_leap":function(year){ // parse this year leap info
                    return this.data.leap( this.data.get_year(year) )
                },
                "leap_month":function(year){
                    var r = this.data.leap( this.data.get_year(year) )
                    return r[0]
                },
                "is_leap":function(year,month){ // check leap
                    var month = month || -1, leapinfo = this.year_leap(year)
                    if(month==-1){
                        return leapinfo[0]
                    } else {
                        return month === leapinfo[0]
                    }
                },
                "days_of_month":function(year,month){ // get special month days
                    var d = this.year(year),
                     ret = ( d[d.length-1] == month )? [d[0], d[month]] : [d[month]]
                    return ret
                },
                "month_days_of_year":function(year){ // all month days of one year
                    var d = this.year(year),leap = d[d.length-1],  ret = d.slice(1,-1)
                    if( leap ){
                        ret.splice(leap,0,d[0]) // insert
                    }
                    return ret
                },
                "last_of_year":function(year){
                    var d=this.year(year),leap=d[d.length-1]
                        ,ret = new LunarDate(year,12)
                    ret.day = (leap==12)?d[0]:d[d.length-2]
                    return ret
                },
                "last_of_calendar":function(){
                    if( this.LAST_OF_CALENDAR ){
                        return this.LAST_OF_CALENDAR
                    }
                    this.LAST_OF_CALENDAR = this.last_of_year(this.data.get_last_year())
                    return this.LAST_OF_CALENDAR
                }
            },
            "format":{
                "year":function(year){
                    return String(year)+LUNAR_DATE_CONSTANT.YEAR
                },
                "month":function(month,leap){
                    return [leap?LUNAR_DATE_CONSTANT.LEAP:''
                            ,LUNAR_DATE_CONSTANT.MONTH_NAMES[n-1]
                            ,LUNAR_DATE_CONSTANT.MONTH].join('')
                },
                "day":function(day){
                    var C = LUNAR_DATE_CONSTANT
                    if( day == 10){
                        return C.TEN_DAYS.slice(0,2)
                    } else if( day % 10 == 0 ){
                        return C.NUMBERS[ parseInt(day/10) -1 ] + C.NUMBERS[9]
                    } else {
                        return C.TEN_DAYS[parseInt(day/10)] + C.NUMBERS[day%10-1]
                    }
                }
            }
            ,"helper":{
                "lunar_count_days":function(lunar){
                    var C = LUNAR_DATE_CONSTANT
                    var days = 0, parse = LunarFunction.parse
                    for (var i = C.LUNAR_DATA_START_YEAE; i < lunar.year; i++) {
                       days += C.DAYS_OF_YEAR[i]
                    }
                    var days_of_months = parse.month_days_of_year(lunar.year)
                        ,end_index = lunar.month - 1
                        ,leap_month = parse.leap_month(lunar.year)
                    if( leap_month ){
                        if( lunar.month > leap_month || 
                            ( lunar.month == leap_month && lunar.leap )){
                            end_index = lunar.month
                        }
                    }
                    days += days_of_months.slice(0,end_index).reduce(function(b,v){
                        return b+v},0)
                    days += lunar.day -1
                    return days
                },
                "cmp":function(a,b){
                    if(a.year!=b.year){
                        return a.year > b.year ? 1 : -1;
                    }
                    if( a.month != b.month ){
                        return a.month > b.month ? 1:-1;
                    }
                    if( Boolean(a.leap) != Boolean(b.leap) ){
                        return a.leap?1:-1;
                    }
                    return a.day - b.day;
                },
                "cmp_date":function(s1,s2){
                    var t = s1.getUTCFullYear() - s2.getUTCFullYear()
                    if( t ){
                        return t
                    }
                    t = s1.getUTCMonth() - s2.getUTCMonth()
                    if( t){ return t}
                    return s1.getUTCDate() - s2.getUTCDate()
                },
                "lunar_next":function(lunar){
                    var y=lunar.year,m=lunar.month,d=lunar.day,l=lunar.leap
                        , parse = LunarFunction.parse
                        , cmp = LunarFunction.helper.cmp
                    if( ! cmp(lunar, parse.last_of_calendar())){
                        throw new Error("out of index")
                    }
                    var ret = new LunarDate(y,m,d,l)

                    if( m == 12 && d >= 29 &&
                     ! cmp(lunar, parse.last_of_year(y)) ){ // last day of year
                        var leap_month = parse.leap_month(y+1)
                        ret = new LunarDate(y+1,1,1, 1==leap_month)
                        return ret
                    }


                    var dinfo = parse.year(y), lm = dinfo[dinfo.length-1]
                        ,month_days = dinfo[m]
                    if(lunar.leap ){
                        if( m != lm ){
                            throw new Error("No this lunar date,month or leap error")
                        }
                        month_days = dinfo[0]
                    }

                    if( d < month_days ){
                        ret.day = d+1
                    }else if(d==month_days){
                        ret.day = 1
                        if( lm == m && !l ){
                            ret.leap = 1
                        }else{
                            ret.month = m+1
                            ret.leap = 0
                        }
                    }else{
                        throw new Error("No this lunar date,day error")
                    }
                    return ret
                },
                "solar_next":function(solar){
                    var y=solar.getUTCFullYear(),m=solar.getUTCMonth()
                        , d = solar.getUTCDate()

                    var ret = new Date(y,m,1+d, TIMEZONE_OFFSET/-60)

                    return ret
                }
            },
            "lunartosolar":function(lunar){
                if(exports.cache_limits){
                    return this.cache.lunartosolar(lunar)
                }else{
                    return this._lunartosolar(lunar)
                }
            },
            "solartolunar":function(solar){
                if(exports.cache_limits){
                    return this.cache.solartolunar(solar)
                }else{
                    return this._solartolunar(solar)
                }
            },
            "cache":{ // use cache on reach cache_limits clear all
                "_" : {"length":0},
                "lunartosolar":function(lunar){
                    var cache = LunarFunction.cache._
                        , l = lunar.toDataString();
                    if( l in cache ){
                        return cache[l];
                    }
                    if( cache.length == exports.cache_limits ){
                        cache = {"length":0};
                    }
                    var solar = LunarFunction._lunartosolar(lunar)
                    cache.length ++;
                    cache[l] = solar;
                    return cache[l];
                },
                "solartolunar":function(solar){
                    var cache = LunarFunction.cache._
                        , s = solar.toISOString().slice(0,10)
                    if( s in cache ){
                        return cache[s];
                    }
                    if( cache.length == exports.cache_limits ){
                        cache = {"length":0};
                    }
                    var lunar = LunarFunction._solartolunar(solar)
                    cache.length ++;
                    cache[s] = lunar;
                    return cache[s];
                }
            },
            "_lunartosolar":function(lunar){
                var count_days = LunarFunction.helper.lunar_count_days(lunar)
                return new Date(1899,1,10+count_days,TIMEZONE_OFFSET/-60)
            },
            "_solartolunar":function(solar){
                var C = LUNAR_DATE_CONSTANT
                    , START_SOLAR=C.LUNAR_DATA_STAER_SOLAE
                var t = solar.getTime() - START_SOLAR.getTime()
                    , count_days = Math.floor(t/86400000)
                    , Sy = START_SOLAR.getUTCFullYear(), Sm = START_SOLAR.getUTCMonth()
                    , Sd = START_SOLAR.getUTCDate()
                    , Ns = new Date(Sy, Sm ,Sd+count_days,TIMEZONE_OFFSET/-60)
                if( this.helper.cmp_date(Ns, solar) != 0 ){
                //console.warn(Ns,solar, this.helper.cmp_date(Ns,solar));
                    throw new Error('count days error:_solartolunar')
                }

                var y=solar.getUTCFullYear(),m=solar.getUTCMonth(),d=solar.getUTCDate()
                var lunar_days = 0
                for(var i=y-1;i>=C.LUNAR_DATA_START_YEAE;i--){
                   lunar_days += C.DAYS_OF_YEAR[i]
                }
                var cur_count = lunar_days, cur_year = y, cur_month = 0, cur_day = d
                if( cur_count > count_days ){
                    cur_count -= C.DAYS_OF_YEAR[cur_year-1]
                    cur_year --;
                }else if( cur_count < count_days ){
                    if( cur_count + C.DAYS_OF_YEAR[cur_year] <= count_days ){
                        cur_count += C.DAYS_OF_YEAR[cur_year]
                        cur_year ++;
                    }
                } else {
                    return new LunarDate(cur_year,1,1)
                }
                var parse = LunarFunction.parse
                    , days_of_months = parse.month_days_of_year(cur_year)
                    , leap_month = parse.leap_month(cur_year)
                for(var i=0,l=days_of_months.length;i<l;i++){
                    cur_month = (!leap_month||i<leap_month)?i+1:i;
                    var v = days_of_months[i]
                    if( cur_count + v > count_days){
                        return new LunarDate(cur_year,cur_month,count_days-cur_count+1,leap_month&&i==leap_month)
                    }else if( cur_count + v == count_days ){
                        var _leap = 0
                        if( leap_month && i+1 == leap_month){
                            _leap = 1
                        } else {
                            cur_month ++
                        }
                        return new LunarDate(cur_year,cur_month, 1, _leap)
                    }  else {
                        cur_count += v
                    }
                }
                throw new Error('out of range')
            }
        };


        LunarFunction.parse.data.init(); // must call this, to prepare parse

        exports.cache_limits = 1000 // 0 means no cache
        exports.LunarDate = LunarDate
        exports.LunarFunction = LunarFunction

        LunarDate.prototype.tosolar = function(){
            return LunarFunction.lunartosolar(this)
        }


        LunarDate.fromsolar = function(s){
            if(!s){
                s = new Date();
                s.setHours(s.getHours()+(TIMEZONE_OFFSET/-60))
            }
            return LunarFunction.solartolunar(s)
        }


        return exports

    }) // End of define

})(('define' in window)?define:null,window) // second is exports
