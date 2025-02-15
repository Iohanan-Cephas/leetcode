#include <stdio.h>

int duplicate_values(int arr[], int size){
    for(int i = 0; i < size; i++){
        for(int j = size-1; j > i; j--){
            if(arr[i] == arr[j]){
                return 1;
            }
        }
    }
    return 0;
}

int main(){
    
    int arr[] = {1,2,3,5};
    int size = sizeof(arr)/4;
    
    int result = duplicate_values(arr, size);
    
    if(result == 1){
        printf("True\n");
    }else{
        printf("False\n");
    }
    
    return 0;
}
