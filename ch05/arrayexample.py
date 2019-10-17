# Kelvin modified on Oct 17, 2019
# Chapter 5: Array-Based Sequences
# 基于数组的序列
# /Users/Algorithms/python/kelvin-practice/ch05

## 5.1 Python’s Sequence Types
# Python’s various “sequence” classes, namely the built-in list(列表类), tuple(元组类), and str classes(字符串类).
# Python元组和Python列表数据类似，都是线性表。唯一不同的是，Python元组赋值后所存储的数据不能被程序修改，可以将元组看作是只能读取数据不能修改数据的列表。

## 5.2 Low-Level Arrays

## 5.2.1 Referential Arrays

# shallow copy & deep copy
# However, with a syntax such as backup=list(primes), produces a new list that is a shallow copy. 
# If elements are immutable, this point is moot. 
# 
# If the contents of the list were of a mutable type, a deep copy, meaning a new list with new elements, 
# can be produced by using deep copy function from the copy module.


## 5.2.2 Compact Arrays in Python   紧凑数组
# In the introduction to this section, we emphasized that strings are represented using an array of characters (not an array of references). 
# We will refer to this more direct representation as a compact array because the array is storing the bits that represent the primary data (characters, in the case of strings).

import array
import sys
x = [1, 3, 5, 7, 9]
print("\nsys.getsizeof(x): ", sys.getsizeof(x))
# Primary support for compact arrays is in a module named array. That module defines a class, also named array, providing compact storage for arrays of primitive data types. 
# the type code, i , designates an array of (signed) integers, typically represented using at least 16-bits each.
y = array.array('i', [1, 3, 5, 7, 9])   
print("\nsys.getsizeof(y): ", sys.getsizeof(y))
# sys.getsizeof(x):  112
# sys.getsizeof(y):  84


## Dynamic Arrays and Amortization  动态数组和摊销

# Soultion from the book:
print("\n------ Soultion from the book ------")
data = []
for k in range(300):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}; size in bytes: {1: 4d}".format(a, b))
    data.append(None)

# Length:   0; size in bytes:   72
# Length:   1; size in bytes:  104      104 = 72 + 32 = 72 + 4*8
# Length:   2; size in bytes:  104
# Length:   3; size in bytes:  104
# Length:   4; size in bytes:  104
# Length:   5; size in bytes:  136      136 = 72 + 64 = 72 + 8*8
# Length:   6; size in bytes:  136
# Length:   7; size in bytes:  136
# Length:   8; size in bytes:  136
# Length:   9; size in bytes:  200      200 = 72 + 128 = 72 + 16*8
# Length:  10; size in bytes:  200
# Length:  11; size in bytes:  200
# Length:  12; size in bytes:  200
# Length:  13; size in bytes:  200
# Length:  14; size in bytes:  200
# Length:  15; size in bytes:  200
# Length:  16; size in bytes:  200
# Length:  17; size in bytes:  272      272 = 72 + 200 = 72 + 25*8
# Length:  18; size in bytes:  272
# Length:  19; size in bytes:  272
# Length:  20; size in bytes:  272
# Length:  21; size in bytes:  272
# Length:  22; size in bytes:  272
# Length:  23; size in bytes:  272
# Length:  24; size in bytes:  272
# Length:  25; size in bytes:  272
# Length:  26; size in bytes:  352      352 = 72 + 280 = 72 + 35*8
# Length:  27; size in bytes:  352
# Length:  28; size in bytes:  352
# Length:  29; size in bytes:  352
# Length:  30; size in bytes:  352
# Length:  31; size in bytes:  352
# Length:  32; size in bytes:  352
# Length:  33; size in bytes:  352
# Length:  34; size in bytes:  352
# Length:  35; size in bytes:  352
# Length:  36; size in bytes:  440      440 = 72 + 368 = 72 + 46*8
# Length:  37; size in bytes:  440
# Length:  38; size in bytes:  440
# Length:  39; size in bytes:  440
# Length:  40; size in bytes:  440
# Length:  41; size in bytes:  440
# Length:  42; size in bytes:  440
# Length:  43; size in bytes:  440
# Length:  44; size in bytes:  440
# Length:  45; size in bytes:  440
# Length:  46; size in bytes:  440
# Length:  47; size in bytes:  536
# Length:  48; size in bytes:  536
# Length:  49; size in bytes:  536
# Length:  50; size in bytes:  536
# Length:  51; size in bytes:  536
# Length:  52; size in bytes:  536
# Length:  53; size in bytes:  536
# Length:  54; size in bytes:  536
# Length:  55; size in bytes:  536
# Length:  56; size in bytes:  536
# Length:  57; size in bytes:  536
# Length:  58; size in bytes:  536
# Length:  59; size in bytes:  648
# Length:  60; size in bytes:  648
# Length:  61; size in bytes:  648
# Length:  62; size in bytes:  648
# Length:  63; size in bytes:  648
# Length:  64; size in bytes:  648
# Length:  65; size in bytes:  648
# Length:  66; size in bytes:  648
# Length:  67; size in bytes:  648
# Length:  68; size in bytes:  648
# Length:  69; size in bytes:  648
# Length:  70; size in bytes:  648
# Length:  71; size in bytes:  648
# Length:  72; size in bytes:  648
# Length:  73; size in bytes:  776
# Length:  74; size in bytes:  776
# Length:  75; size in bytes:  776
# Length:  76; size in bytes:  776
# Length:  77; size in bytes:  776
# Length:  78; size in bytes:  776
# Length:  79; size in bytes:  776
# Length:  80; size in bytes:  776
# Length:  81; size in bytes:  776
# Length:  82; size in bytes:  776
# Length:  83; size in bytes:  776
# Length:  84; size in bytes:  776
# Length:  85; size in bytes:  776
# Length:  86; size in bytes:  776
# Length:  87; size in bytes:  776
# Length:  88; size in bytes:  776
# Length:  89; size in bytes:  920
# Length:  90; size in bytes:  920
# Length:  91; size in bytes:  920
# Length:  92; size in bytes:  920
# Length:  93; size in bytes:  920
# Length:  94; size in bytes:  920
# Length:  95; size in bytes:  920
# Length:  96; size in bytes:  920
# Length:  97; size in bytes:  920
# Length:  98; size in bytes:  920
# Length:  99; size in bytes:  920
# Length: 100; size in bytes:  920
# Length: 101; size in bytes:  920
# Length: 102; size in bytes:  920
# Length: 103; size in bytes:  920
# Length: 104; size in bytes:  920
# Length: 105; size in bytes:  920
# Length: 106; size in bytes:  920
# Length: 107; size in bytes:  1080
# Length: 108; size in bytes:  1080
# Length: 109; size in bytes:  1080
# Length: 110; size in bytes:  1080
# Length: 111; size in bytes:  1080
# Length: 112; size in bytes:  1080
# Length: 113; size in bytes:  1080
# Length: 114; size in bytes:  1080
# Length: 115; size in bytes:  1080
# Length: 116; size in bytes:  1080
# Length: 117; size in bytes:  1080
# Length: 118; size in bytes:  1080
# Length: 119; size in bytes:  1080
# Length: 120; size in bytes:  1080
# Length: 121; size in bytes:  1080
# Length: 122; size in bytes:  1080
# Length: 123; size in bytes:  1080
# Length: 124; size in bytes:  1080
# Length: 125; size in bytes:  1080
# Length: 126; size in bytes:  1080
# Length: 127; size in bytes:  1256
# Length: 128; size in bytes:  1256
# Length: 129; size in bytes:  1256
# Length: 130; size in bytes:  1256
# Length: 131; size in bytes:  1256
# Length: 132; size in bytes:  1256
# Length: 133; size in bytes:  1256
# Length: 134; size in bytes:  1256
# Length: 135; size in bytes:  1256
# Length: 136; size in bytes:  1256
# Length: 137; size in bytes:  1256
# Length: 138; size in bytes:  1256
# Length: 139; size in bytes:  1256
# Length: 140; size in bytes:  1256
# Length: 141; size in bytes:  1256
# Length: 142; size in bytes:  1256
# Length: 143; size in bytes:  1256
# Length: 144; size in bytes:  1256
# Length: 145; size in bytes:  1256
# Length: 146; size in bytes:  1256
# Length: 147; size in bytes:  1256
# Length: 148; size in bytes:  1256
# Length: 149; size in bytes:  1456
# Length: 150; size in bytes:  1456
# Length: 151; size in bytes:  1456
# Length: 152; size in bytes:  1456
# Length: 153; size in bytes:  1456
# Length: 154; size in bytes:  1456
# Length: 155; size in bytes:  1456
# Length: 156; size in bytes:  1456
# Length: 157; size in bytes:  1456
# Length: 158; size in bytes:  1456
# Length: 159; size in bytes:  1456
# Length: 160; size in bytes:  1456
# Length: 161; size in bytes:  1456
# Length: 162; size in bytes:  1456
# Length: 163; size in bytes:  1456
# Length: 164; size in bytes:  1456
# Length: 165; size in bytes:  1456
# Length: 166; size in bytes:  1456
# Length: 167; size in bytes:  1456
# Length: 168; size in bytes:  1456
# Length: 169; size in bytes:  1456
# Length: 170; size in bytes:  1456
# Length: 171; size in bytes:  1456
# Length: 172; size in bytes:  1456
# Length: 173; size in bytes:  1456
# Length: 174; size in bytes:  1680
# Length: 175; size in bytes:  1680
# Length: 176; size in bytes:  1680
# Length: 177; size in bytes:  1680
# Length: 178; size in bytes:  1680
# Length: 179; size in bytes:  1680
# Length: 180; size in bytes:  1680
# Length: 181; size in bytes:  1680
# Length: 182; size in bytes:  1680
# Length: 183; size in bytes:  1680
# Length: 184; size in bytes:  1680
# Length: 185; size in bytes:  1680
# Length: 186; size in bytes:  1680
# Length: 187; size in bytes:  1680
# Length: 188; size in bytes:  1680
# Length: 189; size in bytes:  1680
# Length: 190; size in bytes:  1680
# Length: 191; size in bytes:  1680
# Length: 192; size in bytes:  1680
# Length: 193; size in bytes:  1680
# Length: 194; size in bytes:  1680
# Length: 195; size in bytes:  1680
# Length: 196; size in bytes:  1680
# Length: 197; size in bytes:  1680
# Length: 198; size in bytes:  1680
# Length: 199; size in bytes:  1680
# Length: 200; size in bytes:  1680
# Length: 201; size in bytes:  1680
# Length: 202; size in bytes:  1936
# Length: 203; size in bytes:  1936
# Length: 204; size in bytes:  1936
# Length: 205; size in bytes:  1936
# Length: 206; size in bytes:  1936
# Length: 207; size in bytes:  1936
# Length: 208; size in bytes:  1936
# Length: 209; size in bytes:  1936
# Length: 210; size in bytes:  1936
# Length: 211; size in bytes:  1936
# Length: 212; size in bytes:  1936
# Length: 213; size in bytes:  1936
# Length: 214; size in bytes:  1936
# Length: 215; size in bytes:  1936
# Length: 216; size in bytes:  1936
# Length: 217; size in bytes:  1936
# Length: 218; size in bytes:  1936
# Length: 219; size in bytes:  1936
# Length: 220; size in bytes:  1936
# Length: 221; size in bytes:  1936
# Length: 222; size in bytes:  1936
# Length: 223; size in bytes:  1936
# Length: 224; size in bytes:  1936
# Length: 225; size in bytes:  1936
# Length: 226; size in bytes:  1936
# Length: 227; size in bytes:  1936
# Length: 228; size in bytes:  1936
# Length: 229; size in bytes:  1936
# Length: 230; size in bytes:  1936
# Length: 231; size in bytes:  1936
# Length: 232; size in bytes:  1936
# Length: 233; size in bytes:  1936
# Length: 234; size in bytes:  2224
# Length: 235; size in bytes:  2224
# Length: 236; size in bytes:  2224
# Length: 237; size in bytes:  2224
# Length: 238; size in bytes:  2224
# Length: 239; size in bytes:  2224
# Length: 240; size in bytes:  2224
# Length: 241; size in bytes:  2224
# Length: 242; size in bytes:  2224
# Length: 243; size in bytes:  2224
# Length: 244; size in bytes:  2224
# Length: 245; size in bytes:  2224
# Length: 246; size in bytes:  2224
# Length: 247; size in bytes:  2224
# Length: 248; size in bytes:  2224
# Length: 249; size in bytes:  2224
# Length: 250; size in bytes:  2224
# Length: 251; size in bytes:  2224
# Length: 252; size in bytes:  2224
# Length: 253; size in bytes:  2224
# Length: 254; size in bytes:  2224
# Length: 255; size in bytes:  2224
# Length: 256; size in bytes:  2224
# Length: 257; size in bytes:  2224
# Length: 258; size in bytes:  2224
# Length: 259; size in bytes:  2224
# Length: 260; size in bytes:  2224
# Length: 261; size in bytes:  2224
# Length: 262; size in bytes:  2224
# Length: 263; size in bytes:  2224
# Length: 264; size in bytes:  2224
# Length: 265; size in bytes:  2224
# Length: 266; size in bytes:  2224
# Length: 267; size in bytes:  2224
# Length: 268; size in bytes:  2224
# Length: 269; size in bytes:  2224
# Length: 270; size in bytes:  2544
# Length: 271; size in bytes:  2544
# Length: 272; size in bytes:  2544
# Length: 273; size in bytes:  2544
# Length: 274; size in bytes:  2544
# Length: 275; size in bytes:  2544
# Length: 276; size in bytes:  2544
# Length: 277; size in bytes:  2544
# Length: 278; size in bytes:  2544
# Length: 279; size in bytes:  2544
# Length: 280; size in bytes:  2544
# Length: 281; size in bytes:  2544
# Length: 282; size in bytes:  2544
# Length: 283; size in bytes:  2544
# Length: 284; size in bytes:  2544
# Length: 285; size in bytes:  2544
# Length: 286; size in bytes:  2544
# Length: 287; size in bytes:  2544
# Length: 288; size in bytes:  2544
# Length: 289; size in bytes:  2544
# Length: 290; size in bytes:  2544
# Length: 291; size in bytes:  2544
# Length: 292; size in bytes:  2544
# Length: 293; size in bytes:  2544
# Length: 294; size in bytes:  2544
# Length: 295; size in bytes:  2544
# Length: 296; size in bytes:  2544
# Length: 297; size in bytes:  2544
# Length: 298; size in bytes:  2544
# Length: 299; size in bytes:  2544


# Soultion from the jupyter:
import sys

print("\n------ Soultion from the jupyter ------")
data = []
len_container = []
byte_container = []
for k in range(300):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}; size in bytes: {1: 4d}".format(a, b))
    len_container.append(a)
    byte_container.append(b)
    data.append(None)

# Length:   0; size in bytes:   72
# Length:   1; size in bytes:  104      104 = 72 + 32 = 72 + 4*8
# Length:   2; size in bytes:  104
# Length:   3; size in bytes:  104
# Length:   4; size in bytes:  104
# Length:   5; size in bytes:  136      136 = 72 + 64 = 72 + 8*8
# Length:   6; size in bytes:  136
# Length:   7; size in bytes:  136
# Length:   8; size in bytes:  136
# Length:   9; size in bytes:  200      200 = 72 + 128 = 72 + 16*8
# Length:  10; size in bytes:  200
# Length:  11; size in bytes:  200
# Length:  12; size in bytes:  200
# Length:  13; size in bytes:  200
# Length:  14; size in bytes:  200
# Length:  15; size in bytes:  200
# Length:  16; size in bytes:  200
# Length:  17; size in bytes:  272      272 = 72 + 200 = 72 + 25*8
# Length:  18; size in bytes:  272
# Length:  19; size in bytes:  272
# Length:  20; size in bytes:  272
# Length:  21; size in bytes:  272
# Length:  22; size in bytes:  272
# Length:  23; size in bytes:  272
# Length:  24; size in bytes:  272
# Length:  25; size in bytes:  272
# Length:  26; size in bytes:  352      352 = 72 + 280 = 72 + 35*8
# Length:  27; size in bytes:  352
# Length:  28; size in bytes:  352
# Length:  29; size in bytes:  352
# Length:  30; size in bytes:  352
# Length:  31; size in bytes:  352
# Length:  32; size in bytes:  352
# Length:  33; size in bytes:  352
# Length:  34; size in bytes:  352
# Length:  35; size in bytes:  352
# Length:  36; size in bytes:  440      440 = 72 + 368 = 72 + 46*8
# Length:  37; size in bytes:  440
# Length:  38; size in bytes:  440
# Length:  39; size in bytes:  440
# Length:  40; size in bytes:  440
# Length:  41; size in bytes:  440
# Length:  42; size in bytes:  440
# Length:  43; size in bytes:  440
# Length:  44; size in bytes:  440
# Length:  45; size in bytes:  440
# Length:  46; size in bytes:  440      
# Length:  47; size in bytes:  536
# Length:  48; size in bytes:  536
# Length:  49; size in bytes:  536
# Length:  50; size in bytes:  536
# Length:  51; size in bytes:  536
# Length:  52; size in bytes:  536
# Length:  53; size in bytes:  536
# Length:  54; size in bytes:  536
# Length:  55; size in bytes:  536
# Length:  56; size in bytes:  536
# Length:  57; size in bytes:  536
# Length:  58; size in bytes:  536
# Length:  59; size in bytes:  648
# Length:  60; size in bytes:  648
# Length:  61; size in bytes:  648
# Length:  62; size in bytes:  648
# Length:  63; size in bytes:  648
# Length:  64; size in bytes:  648
# Length:  65; size in bytes:  648
# Length:  66; size in bytes:  648
# Length:  67; size in bytes:  648
# Length:  68; size in bytes:  648
# Length:  69; size in bytes:  648
# Length:  70; size in bytes:  648
# Length:  71; size in bytes:  648
# Length:  72; size in bytes:  648
# Length:  73; size in bytes:  776
# Length:  74; size in bytes:  776
# Length:  75; size in bytes:  776
# Length:  76; size in bytes:  776
# Length:  77; size in bytes:  776
# Length:  78; size in bytes:  776
# Length:  79; size in bytes:  776
# Length:  80; size in bytes:  776
# Length:  81; size in bytes:  776
# Length:  82; size in bytes:  776
# Length:  83; size in bytes:  776
# Length:  84; size in bytes:  776
# Length:  85; size in bytes:  776
# Length:  86; size in bytes:  776
# Length:  87; size in bytes:  776
# Length:  88; size in bytes:  776
# Length:  89; size in bytes:  920
# Length:  90; size in bytes:  920
# Length:  91; size in bytes:  920
# Length:  92; size in bytes:  920
# Length:  93; size in bytes:  920
# Length:  94; size in bytes:  920
# Length:  95; size in bytes:  920
# Length:  96; size in bytes:  920
# Length:  97; size in bytes:  920
# Length:  98; size in bytes:  920
# Length:  99; size in bytes:  920
# Length: 100; size in bytes:  920
# Length: 101; size in bytes:  920
# Length: 102; size in bytes:  920
# Length: 103; size in bytes:  920
# Length: 104; size in bytes:  920
# Length: 105; size in bytes:  920
# Length: 106; size in bytes:  920
# Length: 107; size in bytes:  1080
# Length: 108; size in bytes:  1080
# Length: 109; size in bytes:  1080
# Length: 110; size in bytes:  1080
# Length: 111; size in bytes:  1080
# Length: 112; size in bytes:  1080
# Length: 113; size in bytes:  1080
# Length: 114; size in bytes:  1080
# Length: 115; size in bytes:  1080
# Length: 116; size in bytes:  1080
# Length: 117; size in bytes:  1080
# Length: 118; size in bytes:  1080
# Length: 119; size in bytes:  1080
# Length: 120; size in bytes:  1080
# Length: 121; size in bytes:  1080
# Length: 122; size in bytes:  1080
# Length: 123; size in bytes:  1080
# Length: 124; size in bytes:  1080
# Length: 125; size in bytes:  1080
# Length: 126; size in bytes:  1080
# Length: 127; size in bytes:  1256
# Length: 128; size in bytes:  1256
# Length: 129; size in bytes:  1256
# Length: 130; size in bytes:  1256
# Length: 131; size in bytes:  1256
# Length: 132; size in bytes:  1256
# Length: 133; size in bytes:  1256
# Length: 134; size in bytes:  1256
# Length: 135; size in bytes:  1256
# Length: 136; size in bytes:  1256
# Length: 137; size in bytes:  1256
# Length: 138; size in bytes:  1256
# Length: 139; size in bytes:  1256
# Length: 140; size in bytes:  1256
# Length: 141; size in bytes:  1256
# Length: 142; size in bytes:  1256
# Length: 143; size in bytes:  1256
# Length: 144; size in bytes:  1256
# Length: 145; size in bytes:  1256
# Length: 146; size in bytes:  1256
# Length: 147; size in bytes:  1256
# Length: 148; size in bytes:  1256
# Length: 149; size in bytes:  1456
# Length: 150; size in bytes:  1456
# Length: 151; size in bytes:  1456
# Length: 152; size in bytes:  1456
# Length: 153; size in bytes:  1456
# Length: 154; size in bytes:  1456
# Length: 155; size in bytes:  1456
# Length: 156; size in bytes:  1456
# Length: 157; size in bytes:  1456
# Length: 158; size in bytes:  1456
# Length: 159; size in bytes:  1456
# Length: 160; size in bytes:  1456
# Length: 161; size in bytes:  1456
# Length: 162; size in bytes:  1456
# Length: 163; size in bytes:  1456
# Length: 164; size in bytes:  1456
# Length: 165; size in bytes:  1456
# Length: 166; size in bytes:  1456
# Length: 167; size in bytes:  1456
# Length: 168; size in bytes:  1456
# Length: 169; size in bytes:  1456
# Length: 170; size in bytes:  1456
# Length: 171; size in bytes:  1456
# Length: 172; size in bytes:  1456
# Length: 173; size in bytes:  1456
# Length: 174; size in bytes:  1680
# Length: 175; size in bytes:  1680
# Length: 176; size in bytes:  1680
# Length: 177; size in bytes:  1680
# Length: 178; size in bytes:  1680
# Length: 179; size in bytes:  1680
# Length: 180; size in bytes:  1680
# Length: 181; size in bytes:  1680
# Length: 182; size in bytes:  1680
# Length: 183; size in bytes:  1680
# Length: 184; size in bytes:  1680
# Length: 185; size in bytes:  1680
# Length: 186; size in bytes:  1680
# Length: 187; size in bytes:  1680
# Length: 188; size in bytes:  1680
# Length: 189; size in bytes:  1680
# Length: 190; size in bytes:  1680
# Length: 191; size in bytes:  1680
# Length: 192; size in bytes:  1680
# Length: 193; size in bytes:  1680
# Length: 194; size in bytes:  1680
# Length: 195; size in bytes:  1680
# Length: 196; size in bytes:  1680
# Length: 197; size in bytes:  1680
# Length: 198; size in bytes:  1680
# Length: 199; size in bytes:  1680
# Length: 200; size in bytes:  1680
# Length: 201; size in bytes:  1680
# Length: 202; size in bytes:  1936
# Length: 203; size in bytes:  1936
# Length: 204; size in bytes:  1936
# Length: 205; size in bytes:  1936
# Length: 206; size in bytes:  1936
# Length: 207; size in bytes:  1936
# Length: 208; size in bytes:  1936
# Length: 209; size in bytes:  1936
# Length: 210; size in bytes:  1936
# Length: 211; size in bytes:  1936
# Length: 212; size in bytes:  1936
# Length: 213; size in bytes:  1936
# Length: 214; size in bytes:  1936
# Length: 215; size in bytes:  1936
# Length: 216; size in bytes:  1936
# Length: 217; size in bytes:  1936
# Length: 218; size in bytes:  1936
# Length: 219; size in bytes:  1936
# Length: 220; size in bytes:  1936
# Length: 221; size in bytes:  1936
# Length: 222; size in bytes:  1936
# Length: 223; size in bytes:  1936
# Length: 224; size in bytes:  1936
# Length: 225; size in bytes:  1936
# Length: 226; size in bytes:  1936
# Length: 227; size in bytes:  1936
# Length: 228; size in bytes:  1936
# Length: 229; size in bytes:  1936
# Length: 230; size in bytes:  1936
# Length: 231; size in bytes:  1936
# Length: 232; size in bytes:  1936
# Length: 233; size in bytes:  1936
# Length: 234; size in bytes:  2224
# Length: 235; size in bytes:  2224
# Length: 236; size in bytes:  2224
# Length: 237; size in bytes:  2224
# Length: 238; size in bytes:  2224
# Length: 239; size in bytes:  2224
# Length: 240; size in bytes:  2224
# Length: 241; size in bytes:  2224
# Length: 242; size in bytes:  2224
# Length: 243; size in bytes:  2224
# Length: 244; size in bytes:  2224
# Length: 245; size in bytes:  2224
# Length: 246; size in bytes:  2224
# Length: 247; size in bytes:  2224
# Length: 248; size in bytes:  2224
# Length: 249; size in bytes:  2224
# Length: 250; size in bytes:  2224
# Length: 251; size in bytes:  2224
# Length: 252; size in bytes:  2224
# Length: 253; size in bytes:  2224
# Length: 254; size in bytes:  2224
# Length: 255; size in bytes:  2224
# Length: 256; size in bytes:  2224
# Length: 257; size in bytes:  2224
# Length: 258; size in bytes:  2224
# Length: 259; size in bytes:  2224
# Length: 260; size in bytes:  2224
# Length: 261; size in bytes:  2224
# Length: 262; size in bytes:  2224
# Length: 263; size in bytes:  2224
# Length: 264; size in bytes:  2224
# Length: 265; size in bytes:  2224
# Length: 266; size in bytes:  2224
# Length: 267; size in bytes:  2224
# Length: 268; size in bytes:  2224
# Length: 269; size in bytes:  2224
# Length: 270; size in bytes:  2544
# Length: 271; size in bytes:  2544
# Length: 272; size in bytes:  2544
# Length: 273; size in bytes:  2544
# Length: 274; size in bytes:  2544
# Length: 275; size in bytes:  2544
# Length: 276; size in bytes:  2544
# Length: 277; size in bytes:  2544
# Length: 278; size in bytes:  2544
# Length: 279; size in bytes:  2544
# Length: 280; size in bytes:  2544
# Length: 281; size in bytes:  2544
# Length: 282; size in bytes:  2544
# Length: 283; size in bytes:  2544
# Length: 284; size in bytes:  2544
# Length: 285; size in bytes:  2544
# Length: 286; size in bytes:  2544
# Length: 287; size in bytes:  2544
# Length: 288; size in bytes:  2544
# Length: 289; size in bytes:  2544
# Length: 290; size in bytes:  2544
# Length: 291; size in bytes:  2544
# Length: 292; size in bytes:  2544
# Length: 293; size in bytes:  2544
# Length: 294; size in bytes:  2544
# Length: 295; size in bytes:  2544
# Length: 296; size in bytes:  2544
# Length: 297; size in bytes:  2544
# Length: 298; size in bytes:  2544
# Length: 299; size in bytes:  2544

# At the early stage, bytes increased by 32, 64, but later the bytes of the list increased by 320 bytes.


