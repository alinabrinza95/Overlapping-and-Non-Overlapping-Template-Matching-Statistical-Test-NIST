import random,re
import mpmath
def generate_split_compute_nonoverlapping(N,m):
    occurence_vector=dict()
    a=random.getrandbits(pow(2,20))
    M = len(bin(a)[2:]) / N
    print "STEP 1:  The number of independent blocks is: "+ str(N)
    print "STEP 2:  The length in bits of the substring of E to be tested is: "+ str(M)
    with open('bits', 'w') as the_file:
        the_file.write(bin(a)[2:])
    print "STEP 3:  We wrote in the bits file the sequence of " + str(len(bin(a)[2:])) + " bits"
    with open('bits', 'r') as read_file:
        with open('list', 'w') as list_bytes:
            for i in range(len(bin(a)[2:])/M+1):
                list_bytes.write(read_file.read(M) + '\n')
    print "STEP 4:  We partinioned the sequence of bits in " + str(N) + " independent block each of "+str(M)+" bits"
    mean = (M - m + 1.0) / pow(2.0, m)
    print "STEP 5:  The theoretical mean is: " +str(mean)
    variance=M*(1.0/pow(2.0,m)-(2.0*m-1.0)/pow(2.0,2.0*m))
    print "STEP 6:  The variance is: " +str(variance)
    if M<0.01*float(len(bin(a)[2:])):
        print "STOP: We can't continue due to false constraints"
    else:
        target_string=bin(random.getrandbits(m))[2:]
        print "STEP 7:  The target string B is: "+str(target_string)
        with open('list','r') as compute_nonoverlapping:
            i=0
            for line in compute_nonoverlapping:
                block=str(line)
                counter=len(re.findall(str(target_string),block))
                i=i+1
                occurence_vector[i]=counter
        print "STEP 8:  We computed the number of occurences of target string B in each independent block"
        print "STEP 9:  The occurences for each independent block in non-overlapping are: ", occurence_vector
        reference_distribution=0.0
        for j in range(1,N):
            reference_distribution=reference_distribution+pow((float(occurence_vector[j])-mean),2)/variance
        print "STEP 10: The reference distribution is: " + str(reference_distribution)
        P_value=mpmath.gammainc(N/2.0,reference_distribution/2.0 )
        print "STEP 11: The value of P-value is: " +str(P_value)
        if(P_value<0.01):
            print "STOP:    The sequence is non-random in non-overlapping"
        else:
            print"STOP:    The sequence is random in non-overlapping "
generate_split_compute_nonoverlapping(90,10)