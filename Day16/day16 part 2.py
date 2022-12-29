import time
st = time.time()

# Why this works
#   1.  The calculation of each digit is independent.  ie.  Digit 3 can be computed before Digit 1 if you wish
#   2.  For row n,  then first n values in the pattern are zero.  This means that these values don't effect the calculation.
#   3.  For row n (where n >= offset) all values in the pattern after n,  are 1.  This means they can just be summed.

# from this we know
#  1.  Rows before the offset can be ignored (as they are always multiplied with zero)
#  2.  The pattern can be ignored (as all values are 1)
#  3.  Values before the offset can just be removed.

# If we consider the final three rows,  we can see a pattern emerge.
#  row n   =   a,b,c  => a+b+c
#  row n+1 =     b,c  =>   b+c 
#  row n+2 =       c  =>     c
# 
# For performance we can just start by computing the final row,  then compute the previous row by just adding a single digit.


input_signal = "59717513948900379305109702352254961099291386881456676203556183151524797037683068791860532352118123252250974130706958763348105389034831381607519427872819735052750376719383812473081415096360867340158428371353702640632449827967163188043812193288449328058464005995046093112575926165337330100634707115160053682715014464686531460025493602539343245166620098362467196933484413717749680188294435582266877493265037758875197256932099061961217414581388227153472347319505899534413848174322474743198535953826086266146686256066319093589456135923631361106367290236939056758783671975582829257390514211329195992209734175732361974503874578275698611819911236908050184158" *10000
# input_signal = "03036732577212944063491565474664" *10000
# input_signal = "02935109699940807407585447034323" *10000
# input_signal = "03081770884921959731165446850517" *10000
offset = int(input_signal[:7])

input_signal = [int(i) for i in input_signal[offset:]]

for r in range(100):
  running_total = 0
  for row in range(len(input_signal)-1, -1, -1):
    running_total += input_signal[row]
    input_signal[row] = running_total%10
print("".join([str(n) for n in input_signal[:8]]))

elapsed_time = time.time() - st
print('Time:', elapsed_time, 'seconds')