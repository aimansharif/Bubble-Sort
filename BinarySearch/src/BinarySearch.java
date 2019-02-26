
public class Class {
	public static int binarySearch(int[] arr, int left, int right, int x) {
		int mid = (left + right) / 2;
		
		//returns the index at which the number is found 
		if(x == arr[mid]) {
			return mid;
		}
		//searches the left half of the array for the number
		else if(x < arr[mid]) {
			return binarySearch(arr, left, mid - 1, x);
		}
		//searches the right half of the array for the number
		else if(x > arr[mid]) {
			return binarySearch(arr, mid + 1, right, x);
		}
		else {
			return -1; //if not found
		}
	}
}
