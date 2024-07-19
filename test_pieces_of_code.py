from NIST_tests.RunTest import RunTest


def test_numbers(RSA_Private_KEY=()): 

    checks_rsa_key = 0

    #while checks_rsa_key != 2:
    test_for_bigest_block = "True" in str(RunTest.longest_one_block_test(bin(RSA_Private_KEY[2])[:1000000]))
    list_for_distance=[]
    
    if RSA_Private_KEY[0]-RSA_Private_KEY[1] > 0:
            list_for_distance.append(RSA_Private_KEY[0])
            list_for_distance.append(RSA_Private_KEY[1])  
    else:
            list_for_distance.append(RSA_Private_KEY[1])
            list_for_distance.append(RSA_Private_KEY[0])
            
    if list_for_distance[0]-list_for_distance[1] > 3351951982485649274893506249551461531869845:
            test_distance_p_and_q = True
    else:
            test_distance_p_and_q = False

    checks_rsa_key = test_distance_p_and_q + test_for_bigest_block

    return str(RunTest.longest_one_block_test(bin(RSA_Private_KEY[2])[:1000000])), str(test_distance_p_and_q), str(test_distance_p_and_q), str(checks_rsa_key)

print(test_numbers(RSA_Private_KEY=(45354534543135566788998653212345666567890078990087788999000989454566798764456, 543246425652425665256752456, 466900755655655412211215567008990099888990008765212343342123532354456414)))