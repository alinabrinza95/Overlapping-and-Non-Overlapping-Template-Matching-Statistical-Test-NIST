import random,re
import mpmath
def generate_split_compute_overlapping(N,M,K,m,n, target):
    a = random.getrandbits(n)
    occurence_vector=[0,0,0,0,0,0]
    pi_values={0:0.364091, 1:0.185659,2:0.139381,3:0.100571,4:0.0704323,5:0.139865}
    print "STEP 1:  The number bits to be generated  is: " + str(pow(10,6))
    print "STEP 2:  The number of independent blocks is: " + str(N)
    print "STEP 3:  The length in bits of each independent block is: "+str(M)
    print "STEP 4:  The number of degree of freedom is " + str(K)
    with open('overlapping_bits','w') as overlapping:
        overlapping.write(bin(a)[2:])
    print "STEP 5:  We wrote in the overlapping_bits file the sequence of " + str(pow(10,6)) + " bits"
    with open('overlapping_bits', 'r') as read_file:
        with open('overlapping_list', 'w') as list_bytes:
            for i in range(len(bin(a)[2:])/M+1):
                list_bytes.write(read_file.read(M) + '\n')
    print "STEP 6:  We partinioned the sequence of bits in " + str(N) + " independent block each of " + str(M) + " bits"
    print "STEP 7:  We chose the length of the target string to be: " + str(m) +" bits"
    Lambda=(M-m+1.0)/pow(2.0,m)
    print "STEP 8:  The mean is: "+ str(Lambda)
    eta=Lambda/2.0
    print "STEP 9:  Eta value is: "+str(eta)
    if(n<=M*N):
        print "STOP: The constraint n<=M*N is violated"
    else:
        if(N*min(pi_values.values())<5):
            print "STOP: The constraint N*min(pi_values.values())<5 is violated"
        else:
            print "STEP 10: The target string is: "+ str(target)
            regex=input("STEP 11: Enter the regex: ")
            print "STEP 12: The regex is: ",regex
            with open('overlapping_list','r') as compute_overlapping:
                for line in compute_overlapping:
                    counter = 0
                    block = str(line)
                    matches = re.finditer(regex, block)
                    counter = len([int(match.group(1)) for match in matches])
                    if counter==0:
                        occurence_vector[0]=occurence_vector[0]+1
                    if counter==1:
                        occurence_vector[1] = occurence_vector[1] + 1
                    if counter==2:
                        occurence_vector[2] = occurence_vector[2] + 1
                    if counter==3:
                        occurence_vector[3] = occurence_vector[3] + 1
                    if counter==4:
                        occurence_vector[4] = occurence_vector[4] + 1
                    if counter>=5:
                        occurence_vector[5] = occurence_vector[5] + 1
                print "STEP 13: The occurence vector is: "+str(occurence_vector)
            reference_distribution=0
            for i in range(K):
                reference_distribution=reference_distribution+pow((occurence_vector[i]-N*pi_values[i]),2.0)/(N*pi_values[i])
            print "STEP 14: The reference distribution is: "+str(reference_distribution)
            P_value=mpmath.gammainc(N/2.0,reference_distribution/2.0 )
            print "STEP 15: The P-value is: " +str(P_value)
            if(P_value<0.01):
                print "STOP:    The sequence is non-random in overlapping"
            else:
                print "STOP:    The sequence is random in overlapping"
def create_target_regex(m):
    target_string = bin(random.getrandbits(m))[2:]
    compute_regex = "r\'(?=("
    for i in range(m - 1):
        compute_regex = compute_regex + str(target_string[i]) + "{1}"
    compute_regex = compute_regex + "))\'"
    return target_string, compute_regex
target_string=create_target_regex(10)
print "The target string generated is: "+str(target_string[0])
print "The regex for the target string is: "+str(target_string[1])
#generate_split_compute_overlapping(968,1032,5,10, pow(10,6),target_string[0])
