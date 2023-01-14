import java.util.*;
public class Main{
    public static void main(String[] args) {
        int[] chess = new int[] {1,1,2,2,2,8};//체스말의 개수
        int[] input = new int[6];//체스말을 순서대로 입력받는 배열
        int temp = 0;//비교시 사용 temp
        Scanner sc = new Scanner(System.in);
        
        for(int i=0; i<6; i++){//입력
            input[i] = sc.nextInt();
        }
        
        for(int i=0; i<6; i++){//출력
            input[i] = chess[i] - input[i];
            System.out.println(input[i]);
        }
	}
}