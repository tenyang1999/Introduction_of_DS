# problem1(unfinished)
# 多項式乘法
# (x+2*y)(2*x^2-y^2+z)
# (2*x+3*y+4*z)(xy^2+x^2y+z^2)
# (A+2B2)(B+3C3)(2A+B+C)

# input polynomial
poly1 = input("Enter a poly:")
print("Poly is %s" % (poly1))

# preprocess the input
all_token = [] #把*、^移掉
var_list = []
sym_list = []
num_list = []
for i in range(len(poly1)):
    if poly1[i] != "*" and poly1[i] != "^":
        all_token.append(poly1[i])
        if poly1[i] != "1" and poly1[i] != "2" and poly1[i] != "3" and poly1[i] != "4" and poly1[i] != "5" and poly1[i] != "6" and poly1[i] != "7" and poly1[i] != "8" and poly1[i] != "9" and poly1[i] != "0" and poly1[i] != "+" and poly1[i] != "-" and poly1[i] != "(" and poly1[i] != ")" and poly1[i] not in var_list:
            var_list.append(poly1[i]) #抓變數個數
        elif poly1[i] == "+" or poly1[i] == "-" or poly1[i] == "(" or poly1[i] == ")":
            sym_list.append(poly1[i])
        elif poly1[i] not in var_list and poly1[i] not in sym_list:
            num_list.append(poly1[i])

# arrange the input
coef_dict = {}
exp_dict = {}
var_dict = {}
left_par = 0

for j in range(len(all_token)):
    if all_token[j-1] =="(":
        left_par += 1 #判斷多項式個數
        coef_dict["poly"+str(left_par)] = []
        exp_dict["poly"+str(left_par)] = []
        var_dict["poly"+str(left_par)] = []
    if all_token[j] in var_list: #token is a variable
        # var_dict["poly"+str(left_par)].append(all_token[j])
        if all_token[j-1] in var_list: #判斷係數
            pass
        elif all_token[j-1] == "(" or all_token[j-1] == "+" : 
            coef_dict["poly"+str(left_par)].append(1)
        elif all_token[j-1] == "-":
            coef_dict["poly"+str(left_par)].append(-1)
        else:
            if all_token[j-2] in var_list:
                pass
            else:
                coef_dict["poly"+str(left_par)].append(int(all_token[j-1]))


        if all_token[j-1] in sym_list: #判斷指數
            if all_token[j+1] in sym_list: #s+s
                var_dict["poly"+str(left_par)].append(all_token[j])
                exp_dict["poly"+str(left_par)].append(1)
            elif all_token[j+1] in num_list: 
                if all_token[j+2] in var_list: #s+n+v
                    pass
                else: #s+n
                    var_dict["poly"+str(left_par)].append(all_token[j])
                    exp_dict["poly"+str(left_par)].append(int(all_token[j+1]))
            else:
                pass
        elif all_token[j-1] in num_list:
            if all_token[j+1] in sym_list: 
                if all_token[j-2] in var_list: #v+n+s
                    term = all_token[j-2] + all_token[j]
                    var_dict["poly"+str(left_par)].append(term)
                    exp_dict["poly"+str(left_par)].append([int(all_token[j-1]),1])
                else: #n+s
                    var_dict["poly"+str(left_par)].append(all_token[j])
                    exp_dict["poly"+str(left_par)].append(1)
            elif all_token[j+1] in num_list: #n+n
                var_dict["poly"+str(left_par)].append(all_token[j])
                exp_dict["poly"+str(left_par)].append(int(all_token[j+1]))
            else: #n+v
                pass
        else: 
            if all_token[j+1] in num_list: #v+n
                term = all_token[j-1] + all_token[j]
                var_dict["poly"+str(left_par)].append(term)
                exp_dict["poly"+str(left_par)].append([1,int(all_token[j+1])])

# calculate the coefficient,power
result_coef = [] #收集相乘後的係數
for i in coef_dict["poly1"]:
    for j in coef_dict["poly2"]:
        result_coef.append(i*j)

exp_list = list(exp_dict.values())
result_exp = [] #收集相乘後的各項指數
for i in range(len(exp_dict["poly1"])):
    for j in range(len(exp_dict["poly2"])):
        exp = 0
        if var_dict["poly1"][i] in var_dict["poly2"][j]:
            if isinstance(exp_dict["poly2"][j],list):
                if i == 0:
                    exp1 = exp_list[0][i]
                    exp2 = exp_list[1][j]
                    # print([exp_list[0][i] + exp_list[1][j][0],exp_list[1][j][1]])
                    result_exp.append([exp_list[0][i] + exp_list[1][j][0],exp_list[1][j][1]])
                if i == 1:
                    exp1 = exp_list[0][i]
                    exp2 = exp_list[1][j]
                    # print([exp_list[1][j][0],exp_list[0][j] + exp_list[1][j][1]])
                    result_exp.append([exp_list[1][j][0],exp_list[0][j] + exp_list[1][j][1]])
            else:
                if i == j:
                    exp = exp_dict["poly1"][i] + exp_dict["poly2"][j]
                    # print(exp)
                    result_exp.append(exp)
                else:
                    exp = [exp_dict["poly1"][i],exp_dict["poly2"][j]]
                    # print(exp)
                    result_exp.append(exp)
        else:
            if isinstance(exp_dict["poly2"][j],list):
                exp = exp_dict["poly2"][j]
                exp.append(exp_list[0][i])
                # print(exp)
                result_exp.append(exp)
            else:
                exp = [exp_dict["poly1"][i],exp_dict["poly2"][j]]
                # print(exp)
                result_exp.append(exp)

result_var = []
for i in var_dict["poly1"]:
    for j in var_dict["poly2"]:
        if i in j:
            result_var.append(j)
        else:
            var = i+j
            result_var.append(var)

# combine the result
product_result = []
for i in range(len(result_coef)):
    term = ""
    if isinstance(result_exp[i],list):
        for j in range(len(result_exp[i])):
            if result_exp[i][j] == 1:
                res = result_var[i][j]
            else:
                res = result_var[i][j] + str(result_exp[i][j])
            term += res
        if result_coef[i] == 1:
            term = term
        elif result_coef[i] == -1:
            term = "-" + term
        else:
            term = str(result_coef[i]) + term
        product_result.append(term)
    else:
        term = str(result_coef[i]) + result_var[i] + str(result_exp[i])
        product_result.append(term)

# print answer
answer = ""
for i in range(len(product_result)):
    if i == 0:
        answer = product_result[0]
    else:
        if "-" in product_result[i]:
            answer = answer + product_result[i] 
        else:
            answer = answer + "+" + product_result[i]
print(answer)