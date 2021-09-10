import time


t1 = time.time()

M1 =  [[77, 121, 32, 115, 105, 115, 116, 101, 114],
      [32, 105, 115, 32, 118, 101, 114, 121, 32],
      [115, 109, 97, 114, 116, 32, 97, 110, 100],
      [32, 116, 97, 108, 101, 110, 116, 101, 100],
      [32, 119, 101, 32, 97, 114, 101, 32, 115],
      [109, 97, 114, 116, 32, 102, 97, 109, 105],
      [108, 108, 121, 32, 105, 110, 99, 108, 117],
      [114, 115, 32, 119, 101, 32, 110, 101, 101],
      [100, 32, 116, 111, 32, 115, 109, 105, 108],
      [101, 32, 102, 114, 111, 109, 32, 116, 105],
      [109, 101, 32, 116, 111, 32, 116, 105, 109],
      [101, 32, 110, 111, 32, 109, 111, 114, 101],
      [32, 119, 104, 105, 110, 105, 110, 103],
      [84, 111, 111, 32, 109, 97, 110, 121, 32],
      [116, 104, 105, 110, 103, 115, 32, 104, 97],
      [118, 101, 32, 104, 97, 112, 112, 101, 110],
      [101, 100, 32, 68, 101, 117, 116, 115, 99],
      [104, 32, 112, 104, 105, 108, 111, 115],
      [111, 112, 104, 101, 114, 115, 32, 97, 114],
      [101, 32, 116, 111, 112, 32],
      [77, 121, 32, 115, 105, 115, 116, 101, 114],
      [32, 105, 115, 32, 118, 101, 114, 121, 32],
      [115, 109, 97, 114, 116, 32, 97, 110, 100],
      [32, 116, 97, 108, 101, 110, 116, 101, 100],
      [32, 119, 101, 32, 97, 114, 101, 32, 115],
      [109, 97, 114, 116, 32, 102, 97, 109, 105],
      [108, 108, 121, 32, 105, 110, 99, 108, 117],
      [114, 115, 32, 119, 101, 32, 110, 101, 101],
      [100, 32, 116, 111, 32, 115, 109, 105, 108],
      [101, 32, 102, 114, 111, 109, 32, 116, 105],
      [109, 101, 32, 116, 111, 32, 116, 105, 109],
      [101, 32, 110, 111, 32, 109, 111, 114, 101],
      [32, 119, 104, 105, 110, 105, 110, 103],
      [84, 111, 111, 32, 109, 97, 110, 121, 32],
      [116, 104, 105, 110, 103, 115, 32, 104, 97],
      [118, 101, 32, 104, 97, 112, 112, 101, 110],
      [101, 100, 32, 68, 101, 117, 116, 115, 99],
      [104, 32, 112, 104, 105, 108, 111, 115],
      [111, 112, 104, 101, 114, 115, 32, 97, 114],
      [101, 32, 116, 111, 112, 32],
      [77, 121, 32, 115, 105, 115, 116, 101, 114],
      [32, 105, 115, 32, 118, 101, 114, 121, 32],
      [115, 109, 97, 114, 116, 32, 97, 110, 100],
      [32, 116, 97, 108, 101, 110, 116, 101, 100],
      [32, 119, 101, 32, 97, 114, 101, 32, 115],
      [109, 97, 114, 116, 32, 102, 97, 109, 105],
      [108, 108, 121, 32, 105, 110, 99, 108, 117],
      [114, 115, 32, 119, 101, 32, 110, 101, 101],
      [100, 32, 116, 111, 32, 115, 109, 105, 108],
      [101, 32, 102, 114, 111, 109, 32, 116, 105],
      [109, 101, 32, 116, 111, 32, 116, 105, 109],
      [101, 32, 110, 111, 32, 109, 111, 114, 101],
      [32, 119, 104, 105, 110, 105, 110, 103],
      [84, 111, 111, 32, 109, 97, 110, 121, 32],
      [116, 104, 105, 110, 103, 115, 32, 104, 97],
      [118, 101, 32, 104, 97, 112, 112, 101, 110],
      [101, 100, 32, 68, 101, 117, 116, 115, 99],
      [104, 32, 112, 104, 105, 108, 111, 115],
      [111, 112, 104, 101, 114, 115, 32, 97, 114],
      [101, 32, 116, 111, 112, 32],
      [77, 121, 32, 115, 105, 115, 116, 101, 114],
      [32, 105, 115, 32, 118, 101, 114, 121, 32],
      [115, 109, 97, 114, 116, 32, 97, 110, 100],
      [32, 116, 97, 108, 101, 110, 116, 101, 100],
      [32, 119, 101, 32, 97, 114, 101, 32, 115],
      [109, 97, 114, 116, 32, 102, 97, 109, 105],
      [108, 108, 121, 32, 105, 110, 99, 108, 117],
      [114, 115, 32, 119, 101, 32, 110, 101, 101],
      [100, 32, 116, 111, 32, 115, 109, 105, 108],
      [101, 32, 102, 114, 111, 109, 32, 116, 105],
      [109, 101, 32, 116, 111, 32, 116, 105, 109],
      [101, 32, 110, 111, 32, 109, 111, 114, 101],
      [32, 119, 104, 105, 110, 105, 110, 103],
      [84, 111, 111, 32, 109, 97, 110, 121, 32],
      [116, 104, 105, 110, 103, 115, 32, 104, 97],
      [118, 101, 32, 104, 97, 112, 112, 101, 110],
      [101, 100, 32, 68, 101, 117, 116, 115, 99],
      [104, 32, 112, 104, 105, 108, 111, 115],
      [111, 112, 104, 101, 114, 115, 32, 97, 114],
      [101, 32, 116, 111, 112, 32],
      [77, 121, 32, 115, 105, 115, 116, 101, 114],
      [32, 105, 115, 32, 118, 101, 114, 121, 32],
      [115, 109, 97, 114, 116, 32, 97, 110, 100],
      [32, 116, 97, 108, 101, 110, 116, 101, 100],
      [32, 119, 101, 32, 97, 114, 101, 32, 115],
      [109, 97, 114, 116, 32, 102, 97, 109, 105],
      [108, 108, 121, 32, 105, 110, 99, 108, 117],
      [114, 115, 32, 119, 101, 32, 110, 101, 101],
      [100, 32, 116, 111, 32, 115, 109, 105, 108],
      [101, 32, 102, 114, 111, 109, 32, 116, 105],
      [109, 101, 32, 116, 111, 32, 116, 105, 109],
      [101, 32, 110, 111, 32, 109, 111, 114, 101],
      [32, 119, 104, 105, 110, 105, 110, 103],
      [84, 111, 111, 32, 109, 97, 110, 121, 32],
      [116, 104, 105, 110, 103, 115, 32, 104, 97],
      [118, 101, 32, 104, 97, 112, 112, 101, 110],
      [101, 100, 32, 68, 101, 117, 116, 115, 99],
      [104, 32, 112, 104, 105, 108, 111, 115],
      [111, 112, 104, 101, 114, 115, 32, 97, 114],
      [101, 32, 116, 111, 112, 32]]
     

matrix_length = len(M1)

#To print the rows in the Matrix
for i in range(matrix_length):
    print(M1[i])


t2 = time.time()
t = t2 - t1
print("Elapsed time is : ", t, " seconds")
