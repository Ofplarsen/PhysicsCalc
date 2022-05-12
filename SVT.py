import sys
import mpmath
import numpy as np

if __name__ == '__main__':
    dataSolid = np.array([0.299*2, 0.298*2, 0.293*2, 0.300*2, 0.299*2, 0.295*2])

    dataHul = np.array([0.235*2, 0.236*2, 0.230*2, 0.234*2, 0.238*2, 0.238*2])

    stdSolid = np.std(dataSolid, ddof=1)

    stdHul = np.std(dataHul, ddof=1)

    stdErrSolid = stdSolid / np.sqrt(np.size(dataSolid))

    stdErrHul = stdHul / np.sqrt(np.size(dataHul))

    meanSolid = np.mean(dataSolid)

    meanHul = np.mean(dataHul)
    print("Solid cylinder:")
    print("Mean: " + str(meanSolid))
    print("Std: " + str(stdSolid))
    print("StdErr: " + str(stdErrSolid))

    print("")
    print("Hollow cylinder")
    print("Mean: " + str(meanHul))
    print("Std: " + str(stdHul))
    print("StdErr: " + str(stdErrHul))