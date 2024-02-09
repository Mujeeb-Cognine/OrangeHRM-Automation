def build = currentBuild
def buildUrl = build.absoluteUrl

def subject = "Jenkins Build Passed: ${build.fullDisplayName}"
def body = """
    <html>
    <body>
        <p>Dear User,</p>
        <p>The Jenkins build <a href="${buildUrl}">${build.fullDisplayName}</a> has Passed.</p>
        <p>Best regards,<br>Jenkins CI</p>
    </body>
    </html>
"""

return [subject: subject, body: body]
