Train model
python3 model/train.py

Run the analyser

python3 cli/reactopt.py suggest react-app/src/components/UserCard.jsx

Case 1: propsReceived=9, propsUsed=9, isMemoized=true, then in this case the Component is already optimised.

Case 2: propsReceived=9, propsUsed=9, isMemoized=false, then in this case the Component is using all props that are received, but it can create performance bottlenecks if the list is large, then in this case React.memo should be suggested.

Case 3: propsReceived=9, propsUsed=8, isMemoized=true, then in this case the Component has React memo, so that means even if the one unused props starts changing, it will not go ahead and update the whole UserList. It will only update the ones that are changing. In this case, we can leave it as it is.

Case 4: propsReceived=9, propsUsed=8, isMemoized=false, that means React.memo is not used, and that one unused prop can cause issues. So basically the unused props are less, but the component can still be made better. So the suggestion should be to provide React.memo
