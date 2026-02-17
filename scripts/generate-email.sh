#!/bin/bash
# ============================================================
# CFM Corner — Weekly Email Generator
# Usage: ./scripts/generate-email.sh 08
#        ./scripts/generate-email.sh 12
# Output: Desktop/cfm-email-weekNN.html (ready for Mailchimp)
# ============================================================

set -e

WEEK_NUM=$(printf "%02d" "$(echo "$1" | sed 's/^0*//')")
SITE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
WEEK_FILE="$SITE_DIR/content/weeks/${WEEK_NUM}.md"

if [ ! -f "$WEEK_FILE" ]; then
    echo "❌ Week file not found: $WEEK_FILE"
    exit 1
fi

echo "📧 Generating email for Week $WEEK_NUM..."

# --- Extract front matter fields ---
# Use perl instead of sed for proper UTF-8 handling
get_field() {
    perl -CSD -ne "if (/^${1}:\s*\"?(.*?)\"?\s*$/) { print \$1; exit; }" "$WEEK_FILE"
}

TITLE=$(get_field "title")
SCRIPTURE=$(get_field "scripture")
DATES=$(get_field "dates")
IMAGE_ALT=$(get_field "image_alt")
DESCRIPTION=$(get_field "description")
QUICK_SUMMARY=$(get_field "quick_summary")

# Extract charts (title + description pairs)
CHARTS_BLOCK=""
IN_CHARTS=false
while IFS= read -r line; do
    if [[ "$line" =~ ^charts: ]]; then
        IN_CHARTS=true
        continue
    fi
    if $IN_CHARTS; then
        if [[ "$line" =~ ^---$ ]] || [[ "$line" =~ ^[a-z_]+: && ! "$line" =~ ^[[:space:]] ]]; then
            break
        fi
        if [[ "$line" =~ ^[[:space:]]*-[[:space:]]*title: ]]; then
            CHART_TITLE=$(echo "$line" | sed 's/^.*title: *"*//' | sed 's/"*$//')
        fi
        if [[ "$line" =~ ^[[:space:]]*description: ]]; then
            CHART_DESC=$(echo "$line" | sed 's/^.*description: *"*//' | sed 's/"*$//')
            CHARTS_BLOCK="$CHARTS_BLOCK
                <tr>
                    <td valign=\"top\" style=\"padding: 3px 10px 3px 0; color: #d5a93c; font-size: 18px;\">&#8226;</td>
                    <td style=\"padding: 3px 0; font-family: 'Segoe UI', Helvetica, Arial, sans-serif; color: #333; font-size: 16px; line-height: 1.5;\">
                        <strong>$CHART_TITLE</strong> — $CHART_DESC
                    </td>
                </tr>"
        fi
    fi
done < "$WEEK_FILE"

# If no charts, show a placeholder
if [ -z "$CHARTS_BLOCK" ]; then
    CHARTS_BLOCK="
                <tr>
                    <td style=\"padding: 3px 0; font-family: 'Segoe UI', Helvetica, Arial, sans-serif; color: #666; font-size: 16px; line-height: 1.5; font-style: italic;\">
                        Check the website for this week's interactive charts and tools.
                    </td>
                </tr>"
fi

WEEK_URL="https://www.cfmcorner.com/weeks/${WEEK_NUM}/"

# Mailchimp hosted image URLs (permanent)
MC_HEADER="https://mcusercontent.com/6074bb2e8a5b4a52150832446/images/5cf0c4cd-300b-66a8-bab1-2c326c39f2b3.jpg"
MC_FOOTER="https://mcusercontent.com/6074bb2e8a5b4a52150832446/images/0ae702ea-fca6-a65c-501c-5972c12aeaf7.jpg"

# Truncate quick_summary to first two sentences for email intro
INTRO=$(echo "$QUICK_SUMMARY" | sed 's/\([.!?]\) /\1\n/g' | head -3 | tr '\n' ' ')

OUTPUT="$HOME/Desktop/cfm-email-week${WEEK_NUM}.html"

cat > "$OUTPUT" << EMAILEOF
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Come Follow Me Corner — $SCRIPTURE</title>
    <style type="text/css">
        body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
        table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
        img { -ms-interpolation-mode: bicubic; border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; }
        body { margin: 0; padding: 0; width: 100% !important; background-color: #f4f4f0; }
        @media only screen and (max-width: 600px) {
            .email-container { width: 100% !important; }
            .padding-mobile { padding: 20px !important; }
        }
    </style>
</head>
<body style="margin: 0; padding: 0; background-color: #f4f4f0;">

<div style="display: none; max-height: 0; overflow: hidden; font-size: 1px; line-height: 1px; color: #f4f4f0;">
    This week on CFM Corner: $TITLE ($SCRIPTURE)
</div>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #f4f4f0;">
<tr>
<td align="center" style="padding: 20px 10px;">
<table role="presentation" class="email-container" width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">

    <!-- HEADER BANNER -->
    <tr>
        <td align="center" style="padding: 0;">
            <a href="https://www.cfmcorner.com" target="_blank">
                <img src="$MC_HEADER" width="600" alt="Come Follow Me Corner" style="width: 100%; max-width: 600px; display: block;">
            </a>
        </td>
    </tr>

    <!-- NAVY DIVIDER -->
    <tr>
        <td style="background-color: #1e3a4f; height: 4px; font-size: 0; line-height: 0;">&nbsp;</td>
    </tr>

    <!-- WEEK TITLE -->
    <tr>
        <td class="padding-mobile" style="padding: 30px 40px 10px 40px;">
            <h1 style="font-family: Georgia, 'Times New Roman', serif; color: #1e3a4f; font-size: 26px; margin: 0; border-bottom: 2px solid #d5a93c; padding-bottom: 10px;">
                $SCRIPTURE
            </h1>
        </td>
    </tr>

    <!-- WEEK THEME -->
    <tr>
        <td class="padding-mobile" style="padding: 5px 40px 5px 40px;">
            <p style="font-family: Georgia, 'Times New Roman', serif; color: #57899c; font-size: 17px; font-style: italic; margin: 0;">
                $TITLE (Week $WEEK_NUM) &nbsp;|&nbsp; $DATES
            </p>
        </td>
    </tr>

    <!-- LESSON IMAGE — upload to Mailchimp Content Studio each week -->
    <tr>
        <td style="padding: 20px 40px;">
            <img src="https://www.cfmcorner.com/images/weeks/week${WEEK_NUM}.jpg" width="520" alt="$IMAGE_ALT" style="width: 100%; max-width: 520px; display: block; border-radius: 6px; border: 1px solid #e8e8e4;">
        </td>
    </tr>

    <!-- INTRO -->
    <tr>
        <td class="padding-mobile" style="padding: 0 40px 10px 40px;">
            <p style="font-family: 'Segoe UI', Helvetica, Arial, sans-serif; color: #333; font-size: 16px; line-height: 1.6;">
                Happy Sunday study prep! This week's Come Follow Me materials for <strong>$SCRIPTURE</strong> are live on
                <a href="$WEEK_URL" style="color: #57899c;">Come Follow Me Corner</a>.
            </p>
            <p style="font-family: 'Segoe UI', Helvetica, Arial, sans-serif; color: #333; font-size: 16px; line-height: 1.6;">
                $INTRO
            </p>
        </td>
    </tr>

    <!-- STUDY GUIDE -->
    <tr>
        <td class="padding-mobile" style="padding: 0 40px;">
            <h2 style="font-family: Georgia, 'Times New Roman', serif; color: #1e3a4f; font-size: 20px; margin: 20px 0 10px 0;">
                Weekly Insights Study Guide
            </h2>
            <p style="font-family: 'Segoe UI', Helvetica, Arial, sans-serif; color: #333; font-size: 16px; line-height: 1.6;">
                $DESCRIPTION
            </p>
        </td>
    </tr>

    <!-- INTERACTIVE CHARTS -->
    <tr>
        <td class="padding-mobile" style="padding: 0 40px;">
            <h2 style="font-family: Georgia, 'Times New Roman', serif; color: #1e3a4f; font-size: 20px; margin: 25px 0 10px 0;">
                Interactive Charts
            </h2>
            <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin-left: 10px;">
$CHARTS_BLOCK
            </table>
        </td>
    </tr>

    <!-- WEEKLY RESOURCES -->
    <tr>
        <td class="padding-mobile" style="padding: 0 40px 10px 40px;">
            <h2 style="font-family: Georgia, 'Times New Roman', serif; color: #1e3a4f; font-size: 20px; margin: 25px 0 10px 0;">
                Weekly Resources
            </h2>
            <p style="font-family: 'Segoe UI', Helvetica, Arial, sans-serif; color: #333; font-size: 16px; line-height: 1.6;">
                Curated video commentaries with summaries so you can pick what fits your interest and schedule.
            </p>
            <p style="font-family: 'Segoe UI', Helvetica, Arial, sans-serif; color: #57899c; font-size: 16px; line-height: 1.6; font-style: italic;">
                Whether you've got 15 minutes or an hour, there's a path for you. Come study with us!
            </p>
        </td>
    </tr>

    <!-- CTA BUTTON -->
    <tr>
        <td align="center" style="padding: 10px 40px 30px 40px;">
            <a href="$WEEK_URL" style="background-color: #d5a93c; color: #ffffff; font-family: 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 17px; font-weight: bold; text-decoration: none; padding: 14px 36px; border-radius: 6px; display: inline-block;">
                Read This Week's Lesson
            </a>
        </td>
    </tr>

    <!-- FOOTER BANNER -->
    <tr>
        <td align="center" style="padding: 0;">
            <img src="$MC_FOOTER" width="600" alt="Come Follow Me Corner" style="width: 100%; max-width: 600px; display: block;">
        </td>
    </tr>

    <!-- FOOTER -->
    <tr>
        <td style="background-color: #1e3a4f; padding: 25px 40px; text-align: center;">
            <p style="font-family: 'Segoe UI', Helvetica, Arial, sans-serif; color: #ffffff; font-size: 14px; margin: 0 0 5px 0;">
                <a href="https://www.cfmcorner.com" style="color: #d5a93c; text-decoration: none; font-weight: bold;">cfmcorner.com</a>
            </p>
            <p style="font-family: 'Segoe UI', Helvetica, Arial, sans-serif; color: #8caab8; font-size: 12px; margin: 0 0 10px 0;">
                Come Follow Me Corner — by Kymber Brockbank
            </p>
            <p style="font-family: 'Segoe UI', Helvetica, Arial, sans-serif; color: #8caab8; font-size: 11px; margin: 0 0 5px 0;">
                5725 S. Valley Blvd. Ste 5 PMB 266598, Las Vegas, NV 89118-3122
            </p>
            <p style="font-family: 'Segoe UI', Helvetica, Arial, sans-serif; color: #8caab8; font-size: 11px; margin: 0;">
                <a href="*|UNSUB|*" style="color: #8caab8; text-decoration: underline;">Unsubscribe</a> &nbsp;|&nbsp;
                <a href="*|UPDATE_PROFILE|*" style="color: #8caab8; text-decoration: underline;">Update Preferences</a>
            </p>
        </td>
    </tr>

</table>
</td>
</tr>
</table>

</body>
</html>
EMAILEOF

echo "✅ Email generated: $OUTPUT"
echo ""
echo "📋 Next steps:"
echo "   1. Open $OUTPUT in your browser to preview"
echo "   2. Upload the lesson image to Mailchimp Content Studio"
echo "   3. Lesson image auto-set from cfmcorner.com/images/weeks/week${WEEK_NUM}.jpg"
echo "   4. Replace 'CFMClogo.jpg' and 'CFMbannet.jpg' with Mailchimp hosted URLs"
echo "   5. Copy the HTML into Mailchimp: Campaigns → Email → Code your own → Paste in code"
echo ""
