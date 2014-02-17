#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define MAX_SIZE 1000000

int *memo;

void init(){
    memo = malloc(sizeof(int)*(MAX_SIZE + 1));
    memset(memo, 0, MAX_SIZE + 1);
}

bool is_pow2(int n){
    return (n & (n - 1)) == 0;
}

int calc_pow2(int n){
    int x = n, p2 = 0;
    while(x){
        x = x>>1;
        ++p2;
    }
    return p2;
}


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

int cycles_iterative(int n){
    int cycl = 1;
    while(n > 1){
        if((n % 2) == 0){
            n = n/2;
        } else {
            n = (3 * n) + 1;
        }
        cycl++;
    }
    return cycl;
}

void swap(int *a, int *b){
    int t = *a;
    *a = *b;
    *b = t;
}

void destroy(){
    /*Free up memory*/
    free(memo);
}

int main(){
    /*Initialize the memoization table*/
    init();

    int n, m, i, t, cyc, mx;

    /*Read Input*/
    while(scanf("%d %d",&n,&m) == 2){
        mx = 0;
        printf("%d %d", n, m);
        /* If start is greater than end, swap */
        if(n > m) swap(&n,&m);
        for(i = n; i <= m; i++){
            cyc = cycles(i);
            /*Get the max number of cycles*/
            if(cyc >= mx){
                mx = cyc;
            }
        }
        printf(" %d\n", mx);
    }
    /*Destroy memoization table*/
    destroy();
    return 0;
}