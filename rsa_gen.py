import random

def bruteforse_k_for_rsa_d(rsa_phi_num, rsa_e_num):
    ostatok=101010
    rsa_k_num=0
    while ostatok != 0:
        rsa_k_num=rsa_k_num+1
        ostatok=(rsa_k_num*rsa_phi_num+1) % rsa_e_num
    
    return rsa_k_num

def gen_rsa_key(rsa_p_num, rsa_q_num):

    rsa_n_num=rsa_p_num * rsa_q_num
    rsa_phi_num=(rsa_p_num-1) * (rsa_q_num-1)

    rsa_k_num = bruteforse_k_for_rsa_d(rsa_phi_num, 65537)
    rsa_priv_exp = (rsa_k_num*rsa_phi_num+1) // 65537

    return rsa_p_num,rsa_q_num,rsa_n_num,rsa_phi_num,rsa_priv_exp