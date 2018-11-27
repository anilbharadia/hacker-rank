package sorting;

import java.util.*;

public class Solution {
    public static int solution(String s) {
        //Test1
       /* int result=-0;
        Arrays.sort(A);
        for (int i=0;i<A.length;i++){
            if(A[i]%2 != 0){
                result = A[i];
                break;
            }
        }*/
       //Test2
       /*char[] input = String.valueOf(A).toCharArray();
       StringBuffer result =new StringBuffer();
        int len = (int) Math.ceil((double)input.length/2);
         for (int i=0;i<len;i++) {
            result.append(input[i]);
            if(i<input.length-i-1)
                result.append(input[input.length-i-1]);

        }

        return Integer.valueOf(result.toString());*/

       //Test3

        String[] billRows = s.split(Character.toString((char)10));
        Map<String, Long> totalMap = new HashMap<>();
        for(int i = 0 ; i< billRows.length;i++){
            String[] log = billRows[i].split(",");
            String[] date = log[0].split(":");
            long seconds = (Integer.parseInt(date[0])*60) + (Integer.parseInt(date[1])*60) + Integer.parseInt(date[2]);
            if(totalMap.containsKey(log[1])){
                totalMap.put(log[1],totalMap.get(log[1])+seconds);
            }
            else{
                totalMap.put(log[1],seconds);
            }

        }
Map<String, Integer> chargesMap =new HashMap<>();
        Iterator it = totalMap.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry entry = (Map.Entry)it.next();
            if(Integer.valueOf(entry.getValue().toString())>300){
                chargesMap.put(entry.getKey().toString() , Integer.valueOf(entry.getValue().toString())*3);
            }
            else{
                double minutes = Integer.valueOf(entry.getValue().toString())/60;
                chargesMap.put(entry.getKey().toString() , (int) Math.ceil(minutes)*150);
            }
            it.remove();
        }

        Iterator iterator = chargesMap.entrySet().iterator();
        int max=0;
        int sum =0;
        while (iterator.hasNext()) {
            Map.Entry entry = (Map.Entry)iterator.next();
            if(max < Integer.valueOf(entry.getValue().toString())){
                max=Integer.valueOf(entry.getValue().toString());
            }
            sum = sum + Integer.valueOf(entry.getValue().toString());
            iterator.remove();
        }
System.out.println(sum-max);
        return sum-max;

    }
    public static void main(String[] args) {
        int result = solution("00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090");

    }
}