class Solution {

    class TrieNode {
        HashMap < Character, TrieNode > children = new HashMap();
        String word = null;
        public TrieNode() {}
    }

    char[][] board;
    int[] dr = new int[] {0, 1, -1, 0};
    int[] dc = new int[] {1, 0, 0, -1};
    public List < String > findWords(char[][] board, String[] words) {
        TrieNode root = new TrieNode();
        this.board = board;
        for (String word: words) {
            TrieNode node = root;
            for (int i=0; i < word.length(); i++) {
                if (node.children.containsKey(word.charAt(i))) {
                    node = node.children.get(word.charAt(i)); } else {
                    TrieNode newNode = new TrieNode();
                    node.children.put(word.charAt(i), newNode);
                    node = newNode; }
            }
            node.word = word; }

        List < String > ans = new ArrayList();
        for (int r=0; r < board.length; r++) {
            for (int c=0; c < board[0].length; c++) {
                if (root.children.containsKey(board[r][c])) {
                    dfs(ans, root, r, c);}
            }
        }
        return ans;
    }

    private void dfs(List < String > ans, TrieNode parent, int row, int col) {
        Character letter = board[row][col];
        TrieNode currNode = parent.children.get(letter);

        if (currNode.word != null) {
            ans.add(currNode.word);
            currNode.word = null; 
        }

        board[row][col] = '#';
        for (int i=0; i < 4; ++i) {
            int newRow = row + dr[i];
            int newCol = col + dc[i];
            if (newRow >= 0 && newRow < board.length && newCol >= 0
                && newCol < board[0].length &&
                currNode.children.containsKey(board[newRow][newCol])) {
                dfs(ans, currNode, newRow, newCol); 
            }
        }
        board[row][col] = letter; 
    }
}
