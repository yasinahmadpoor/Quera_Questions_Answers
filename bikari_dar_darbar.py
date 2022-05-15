def fillstring(str_hash,sum_str):
    """This function get the string that have one hash tag (ie. str_hash) and other string (ie. str)
    and compare both of them and replace hash tag with n hash tag. n equal to length of str minus one
    Example: str_hash = #35
                  str = 97635 
            return --> new_str = ###35"""
                    
    num_hash = len(sum_str) - len(str_hash) + 1
    numhash = num_hash*"#"
    new_str = str_hash.replace("#", numhash )
    return new_str
	
def diffstr(new_str,sum_str):
    """This function compare difference between <new_str> and <str> and return the difference portion
    Example: new_hash = ###35
                  str = 97635       
            return --> diff_str = 976"""
            
    diff_str = ""
    for i in range(len(new_str)):
        if new_str[i] != sum_str[i]:
            diff_str += sum_str[i]
    return diff_str
	
def validate(str_hash, str,diff_str):
    """This function check whether value of two side of '=' is equal or not
    for example if 100 + #5 = 120 then there is no equivalent for # and function return False
    but if 100 + #0 = 120 then # equal to 2 and function return True"""
    
    result = str_hash.replace("#",diff_str)
    if result == str:
        return True,result
    else:
        return False,result
    
def main():
    """In this function first check that hash tag lie in which side and then seperate number with hash tag and add or
    subtract two other number. then use fillstring and diffstr and validate function respectively and finally 
    return the result.
    for example we input   -->  1000 + #0 = 1200. 
    first we split two side of equal sign and in this case we see that hash tag lie in left side of equal 
    and right side of plus therefor:
    str_hash = #0
    sum_str = 1200 - 1000 = 200
    new_str = ##0
    diff_str = 20
    result = 200  --> the number with hash tag displaced by result so (#0 -->200)
    validation_flag = True
    and finally return --> 1000 + 200 = 1200"""
    
    left_num, right_num = input().split("=")
    if left_num.find("#") == -1:
        str_hash = right_num.strip(" ")
        sum_str = str(eval(left_num))
        new_str = fillstring(str_hash, sum_str)
        diff_str = diffstr(new_str, sum_str)
        validation_flag, result = validate(str_hash, sum_str,diff_str)
        if validation_flag:
            print(left_num + '=', result)
        else:
            print(-1)
    else:
        left_of_plus_num, right_of_plus_num = left_num.split("+")
        if left_of_plus_num.find("#") == -1:
            str_hash = right_of_plus_num.strip(" ")
            sum_str = str(eval(right_num + "-" + left_of_plus_num))
            new_str = fillstring(str_hash, sum_str)
            diff_str = diffstr(new_str, sum_str)
            validation_flag, result = validate(str_hash, sum_str,diff_str)
            if validation_flag:
                print(left_of_plus_num + '+',result,'=' + right_num)
            else:
                print(-1)
        else:
            str_hash = left_of_plus_num.strip(" ")
            sum_str = str(eval(right_num + "-" + right_of_plus_num))
            new_str = fillstring(str_hash, sum_str)
            diff_str = diffstr(new_str, sum_str)
            validation_flag, result = validate(str_hash, sum_str,diff_str)
            if validation_flag:
                print(result,'+' + right_of_plus_num + '=' + right_num)
            else:
                print(-1) 

if __name__ == '__main__':
    main()