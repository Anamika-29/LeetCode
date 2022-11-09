class StockSpanner {
public:
    StockSpanner() {
        // maintain a monotonic stack for stock entry
        
		// definition of stock entry:
        // first parameter is price quote
        // second parameter is price span
    }
    
    int next(int price) {
        
        int curPrice = price;
        int curSpan = 1;
        
        // Compute price span in stock data with monotonic stack
        while( stack.size() && stack.back().first <= price ){
            
            auto [prevPrice, prevSpan] = stack.back();
            
            stack.pop_back();
            
            // update current price span with history data in stack
            curSpan += prevSpan;
        }
        
        // update latest price quote and price span
        stack.push_back( pair<int, int>{curPrice, curSpan} );
        
        return curSpan;
    }
private:
    vector< pair<int, int> > stack;
};