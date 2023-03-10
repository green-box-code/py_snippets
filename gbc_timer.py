import time as t

def start():
    global _start 
    _start = t.monotonic()
    return _start

def current():
    global _current    
    _current = t.monotonic() - _start
    return _current

def elapsed():
    global _end 
    _end = t.monotonic() - _start
    return _end

def reset():
    global _start
    _start = 0.0
    global _current
    _current = 0.0
    global _end
    _end = 0.0
    
# For Testing
# ====================================================
print(f'Start: {start()}')
t.sleep(3)
print(f'Current Elapsed: {current()}')
t.sleep(4)
print(f'Total Elapsed: {end()}')

reset()
    _start = 0.0
    global _current
    _current = 0.0
    global _end
    _end = 0.0

print(f'Start: {start()}')
t.sleep(3)
print(f'Current Elapsed: {current()}')
t.sleep(4)
print(f'Total Elapsed: {end()}')

reset()
# ====================================================
