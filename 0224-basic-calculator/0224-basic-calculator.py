class Solution {
public:
   int calculate(string s) {
            
    int value = 0;
    int res = 0;
    int sign = 1;
    stack<int> stk;
    stack<int> stksing;

    
    for(char c : s){
        if(c >= '0' && c <= '9'){
            value = value* 10 + (c-'0');
        }else if(c == '+'){
            res += sign * value;
            value = 0;
            sign = 1;
        }else if(c == '-'){
            res += sign * value;
            value = 0;
            sign = -1;
        }else if(c == '('){
            stk.push(res);
            stksing.push(sign);

            res = 0; 
            sign = 1; 
        }else if(c == ')'){
            res += sign * value;
            res *= stksing.top(); stksing.pop();
            res += stk.top(); stk.pop();
            value = 0; 

        }
    }
    return res + sign * value;
}
};