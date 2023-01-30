#include <stdio.h>
#include <string.h>

int f1(int a,int b){
    return (a||!b) + (~a&b) ; 
}

float f2(int num){
    float t = (float)num/2 + num%2 + 1.0/num;
    return t ;
}

int f3(){
    enum FOOD {fish=-1,eggs,meat=3,milk,bean};
    return(eggs+milk)/2>milk?fish:bean;
}

int f4(int n){
    int sum=0;
    for(int i=0;i<n;i++){
        if(i<3)continue;
        sum+=i;
    }
    return sum ; 
}

int f5(char* s){
    int i=0,t=0;
    while(s[i]!='\0'){
        switch(s[i]){
            case 's':t+=1;
                break;
            case 'c':t+=2;
                break;
            case 'e':t+=3;
            default: t+=1;
                break;
        }
        i++;
    }
    return t ;
}

int f6(int x[3], int y[3][3]){
    int t=0,n=3;
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            t+=x[i]*y[i][j];    
    return t;
}

char* f7(char s1[],char s2[]){
    char s[20] = "";
    strncat(s,s1,4); // Hell
    strcat(s,s2); // HellWorld!
    strncpy(s1,s,10); // HellWorld!
    return s1;
}

int main(int argc,char *argv[]){
    int a[3][3] = {{1,1,1},{2,2,2},{3,3,3}};
    int b[3] = {1,2,2};
    char s1[] = "Hello",s2[]="World!";

    printf("%d\n",f1(1,2)); // 3 
    printf("%3.1f\n",f2(5)); //3.7
    printf("%d\n",f3()); //5
    printf("%d\n",f4(5)); // 7 
    printf("%d\n",f5("science")); //5
    printf("%d\n",f6(b,a)); //33
    printf("%s\n",f7(s1,s2)); // HellWorld!
    return 0;
}

