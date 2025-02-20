from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf_from_text(text, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 10)
    
    # Start writing text from the top of the page
    y_position = height - 40
    
    # Write the text, line by line
    for line in text.splitlines():
        c.drawString(40, y_position, line)
        y_position -= 12  # Move down a bit for the next line
        
        # Check if we need a new page
        if y_position < 40:
            c.showPage()  # Start a new page
            c.setFont("Helvetica", 10)
            y_position = height - 40
    
    c.save()

text = "This is the text you want to include in your PDF"  # Replace with actual text
output_pdf = "/Users/giangdinh/Documents/projects/hackathon/output.pdf"
create_pdf_from_text(text, output_pdf) 
