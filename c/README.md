
1) Iterative version:
This version of the program finds the number of cycles exactly as described in the UVa problem statement.

    while(n > 1){
        if((n % 2) == 0){
            n = n/2;
        } else {
            n = (3 * n) + 1;
        }
        cycl++;
    }

My best time for solving this 0.569 s

2) Recursive Version:

    int cycles(int n){
       if(n > 1){
          return 1 + cycles(n % 2 == 0 ? n >>1 : 3*n + 1);
       }
       return 1;
       }
    }

I didn't submit any solution for this version.


Computing f(10) will proceed as follows:

    f(10) = f(5) + 1
    f(5) = f(16) + 1
    f(16) = 1 + f(8)
    f(8) = 1 + f(4)
    f(4) = 1 + f(2)
    f(2) = 1 + 1

Now, computing f(20) will proceed as follows:


     f(20) = 1 + f(10)
     f(10) = f(5) + 1
     f(5) = f(16) + 1
     f(16) = 1 + f(8)
     f(8) = 1 + f(4)
     f(4) = 1 + f(2)
     f(2) = 1 + 1


Clearly, there are overlapping sub-problems when Collatz's conjuncture is calculated for different numbers. Instead of repeatedly calculating the number of cycles for numbers that have been already computed, we can do memoization and save a lot of computation time at the cost of space.


3) Memoized Version:

      int cycles(int n){
        int ans = 0;
        /*Check if the result has been already computed*/
        if((n > 1) && (n <= MAX_SIZE) && (memo[n] != 0)){
            return memo[n];
        } else if (n > 1){
            /*If n is a power of 2, the number of cycles will be equal to the x 
            where x = log(n) note that the base of log is 2*/
            if(is_pow2(n)){
                ans = calc_pow2(n);
            } else {
                ans = 1 + ((n % 2) == 0 ? cycles(n >> 1) : cycles( 3 * n + 1));
            }
            /*Save in the array if n is less than 1000000*/
            if(n <= MAX_SIZE){
                memo[n] = ans;
            }
            return ans;
        }
        else{
            return 1;
        }    
      }
This version saves the intermediate results in the memoization table and looks up before computing for n. Also, this version computes the value of cycle only for required numbers.


My best time for solving the problem with this version was 0.028s (Rank 1798). 


One other way of solving this would be to pre-process and find all the values of cycles for all the numbers in the range 1 to 1000000 and then just lookup for the values from the pre-processed array. i.e., build the memoization table bottom up. But here we will be computing cycle length for numbers which may or may not be required for the solution. The time consumed could be more than the previous version.