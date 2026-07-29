s = "0123456789abcdefghij"
print(f" 1| {s=}, {len(s)=}")
print(f" 2| {s[2]=}")  # A single character (element).
print(f" 3| {s[-3]=}")  # char at end-pos=length-3
print(f" 4| {s[2:4]=}")  # start- (incl.), end-pos (excl.)
print(f" 5| {s[:4]=}")  # start=0, end-pos=4 (excl.)
print(f" 6| {s[4:]=}")  # start=4, end-pos=length
print(f" 7| {s[-4:-2]=}")  # start=length-4, end-pos=length-2
print(f" 8| {s[-2:-4:-1]=}")  # start=length-4, end-pos=length-2
print(f" 9| {s[-1:]=}")  # start=length-1, end-pos=length
print(f"10| {s[3:-2]=}")  # start=3, end-pos=-2
print(f"11| {s[::2]=}")  # start=0, end-pos=length, step=2
