books={}
n=int(input("enter no of books"))
for i in range (n):
    title=input("Enter title of the book").strip()
    author=input("enter author of the book: ").strip()
    year=input("enter year : ").strip
    books[title]={"Author":author, "Year": year}
print(books)
for key,info in books.items():
    print(f"Title: {key}")
    print(f"Author : {info['Author']}")
    print(f"Year : {info['Year']}")
l=list(books.keys())
l.sort()
lst=l
key=input("Enter book title to search : ").strip()
low=0
high=n-1
found=0
while low<=high:
    mid=(high+low)//2
    if(key==lst[mid]):
        found=1
        break
    elif lst[mid]>key:
        high=mid-1
    else:
        low=mid+1
if found==0:
    print("Book not found!")              
else:
    print("Book found!") 
    book = books[key]
    print(f"Author: {book['Author']}")
    print(f"Year: {book['Year']}")   
    
de=input("\nEnter book title to delete : ")
if de in books:
    del books[de]   
    print(f"Book '{de}' deleted successfully.")
else:
    print(f"Book titled '{de}' not found. Cannot delete.") 