class Solution {

    int[] dr = new int[] { 0, -1, 0, 1 };
    int[] dc = new int[] { 1, 0, -1, 0 };
    int ans = 0;

    public int uniquePathsIII(int[][] grid) {
        int R = grid.length;
        int C = grid[0].length;

        int todo = 0;
        int sr = 0, sc = 0;
        int tr = 0, tc = 0;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (grid[r][c] != -1) {
                    todo++;
                }

                if (grid[r][c] == 1) {
                    sr = r;
                    sc = c;
                } else if (grid[r][c] == 2) {
                    tr = r;
                    tc = c;
                }
            }
        }

        ans = 0;
        dfs(sr, sc, tr, tc, grid, todo);
        return ans;
    }

    public void dfs(int sr, int sc, int tr, int tc, int[][] grid, int todo) {
        todo--;
        if (todo < 0)
            return;
        if (sr == tr && sc == tc) {
            if (todo == 0)
                ans++;
            return;
        }

        int R = grid.length;
        int C = grid[0].length;
        grid[sr][sc] = 3;
        for (int k = 0; k < 4; k++) {
            int nr = sr + dr[k];
            int nc = sc + dc[k];
            if (nr >= 0 && nr < R && nc >= 0 && nc < C) {
                if (grid[nr][nc] == 0 || grid[nr][nc] == 2) {
                    dfs(nr, nc, tr, tc, grid, todo);
                }
            }
        }
        grid[sr][sc] = 0;
    }
}