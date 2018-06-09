import datetime as dt

import misc_functions as mf


rt = 0 # rate         e.g. 0.0140
pc = 1 # percent      e.g. 1.40 %
bp = 2 # basis points e.g. 140 bp

idButton1 = 0
idButton2 = 1
idButton3 = 2
idButton4 = 3

oneMonth    = dt.timedelta(days = 30)
threeMonths = dt.timedelta(days = 91)
sixMonths   = dt.timedelta(days = 182)
oneYear     = dt.timedelta(days = 365)
threeYears  = dt.timedelta(days = 3*365)
tenYears    = dt.timedelta(days = 10*365)
strOneMonth = 'time: 1 m'
strThreeMonths = 'time: 3 m'
strSixMonths   = 'time: 6 m'
strOneYear     = 'time: 1 y'
strThreeYears  = 'time: 3 y'
strTenYears    = 'time: 10 y'

today       = dt.date.today()

fivePc       = 5.0
tenPc        = 10.0
twentyFivePc = 25.0
fiftyPc      = 50.0
strFivePc       = '+/- 5.0%'
strTenPc        = '+/- 10.0%'
strTwentyFivePc = '+/- 25.0%'
strFiftyPc = '+/- 50.0%'

td = 0 # 10 days
fw = 1 # 4 weeks
tm = 2 # 3 months
strMTenDays     = 'Mov: 10 d'
strMFourWeeks   = 'Mov: 4 w'
strMThreeMonths = 'Mov: 3 m'
mTenDays     = 10
mFourWeeks   = 20
mThreeMonths = 65
mDur = []
mDur.append(mTenDays)
mDur.append(mFourWeeks)
mDur.append(mThreeMonths)

strTwenty = '20 bins'
strThirty = '30 bins'
strFifty  = '50 bins'
twenty = 20
thirty = 30
fifty  = 50
