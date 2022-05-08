/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {
    Queue<Integer> q = new LinkedList();

    public NestedIterator(List<NestedInteger> nestedList) {
        fillup(nestedList);
    }

    @Override
    public Integer next() {
        if(!q.isEmpty())
            return (Integer)q.poll();
            
        return null;
    }

    @Override
    public boolean hasNext() {
        return !q.isEmpty();
    }
    
    private void fillup(List<NestedInteger> nestedlist)
    {
        if(nestedlist == null)
            return;
        
        for(NestedInteger member:nestedlist)
        {
            if(member.isInteger())
            {
                q.offer(member.getInteger());
            }
            else
            {
                fillup(member.getList());
            }
        }
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */