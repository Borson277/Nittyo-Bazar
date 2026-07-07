import re

with open("app/src/main/java/com/example/ui/screens/HomeScreen.kt", "r") as f:
    content = f.read()

content = content.replace(
    'Text("Total products: ${products.size}, Categories: ${categories.size}", color = Color.Red, fontSize = 20.sp)\n            // Categories Section',
    '// Categories Section'
)

with open("app/src/main/java/com/example/ui/screens/HomeScreen.kt", "w") as f:
    f.write(content)
