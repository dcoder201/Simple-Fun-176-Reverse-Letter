def reverse_letter(string):
    #do your magic here
    res=''
    for i in string[-1::-1]:
        if i.isalpha():
            res+=i
    return(res)
 
test.describe("Basic test")

test.assert_equals(reverse_letter("krishan"),"nahsirk")

test.assert_equals(reverse_letter("ultr53o?n"),"nortlu")

test.assert_equals(reverse_letter("ab23c"),"cba")

test.assert_equals(reverse_letter("krish21an"),"nahsirk")
