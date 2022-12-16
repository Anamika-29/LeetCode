class MyQueue {
public:
    // Push element x to the back of queue...
    void push(int x) {
        in_stk.push(x);
    }
	// Remove the element from the front of the queue and returns it...
    int pop() {
        peek();
        const int val = out_stk.top();
        out_stk.pop();
        return val;
    }
	// Get the front element...
    int peek() {
        if (out_stk.empty())
        while (!in_stk.empty())
            out_stk.push(in_stk.top()), in_stk.pop();
        return out_stk.top();
    }
	// Return whether the queue is empty...
    bool empty() {
        return in_stk.empty() && out_stk.empty();
    }
private:
    stack<int> in_stk;
    stack<int> out_stk;
};


/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */