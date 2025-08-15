public static int findEvenIndex(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        if (Arrays.stream(arr, 0, i).sum() ==
            Arrays.stream(arr, i + 1, arr.length).sum()) {
            return i;
        }
    }
    return -1;
}