class Solution {
    public int shortestPath(int[][] grid, int k) {
        if (grid.length == 0) return 0
        Map < String, Integer > map = new HashMap <> ()
        boolean visited[][] = new boolean[grid.length][grid[0].length]
        int min = dfs(grid, 0, 0, k, map, visited)
        return min == Integer.MAX_VALUE ? - 1: min
    }

    int[] row = {1, -1, 0, 0}
    int[] col = {0, 0, 1, -1}
    private int dfs(int[][] grid, int startI, int startJ, int k, Map < String, Integer > map, boolean visited[][]) {
        if (k < 0) return Integer.MAX_VALUE
        if (startI == grid.length-1 & & startJ == grid[0].length-1) {
            return 0
        }
        String key = startI + "_" + startJ + "_" + k
        if (map.containsKey(key)) {
            return map.get(key)
        }

        if (visited[startI][startJ]) return Integer.MAX_VALUE
        visited[startI][startJ] = true

        int min = Integer.MAX_VALUE
        for (int i=0
             i < 4
             i++) {
            int currRow = startI + row[i]
            int currCol = startJ + col[i]
            if (isSafe(grid, currRow, currCol)) {
                int temp = Integer.MAX_VALUE
                if (grid[currRow][currCol] == 1) {
                    if (k > 0) {
                        temp = dfs(grid, currRow, currCol, k-1, map, visited)
                    } else {
                        continue
                    }
                } else {
                    temp = dfs(grid, currRow, currCol, k, map, visited)
                }

                if (temp != Integer.MAX_VALUE) {
                    min = Math.min(min, temp + 1)
                }

            }
        }
        visited[startI][startJ] = false
        map.put(key, min)
        return min
    }

    boolean isSafe(int grid[][], int i, int j) {
        return i >= 0 & & j >= 0
        & & i < grid.length & & j < grid[0].length
    }

}
