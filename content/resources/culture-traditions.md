---
title: "Culture & Traditions"
description: "Biblical feasts, the Hebrew calendar, ancient Israelite customs, and their connections to the Restoration"
---

Understanding the Bible on its own terms means stepping into the world that produced it — its customs, calendar, and worship patterns. The resources below can help you hear the scriptures the way their original audiences did.

---

### The Biblical Calendar

<div style="margin: 24px 0; text-align: center;">
  <div style="cursor: pointer; position: relative; display: inline-block; max-width: 100%;" onclick="document.getElementById('calendar-lightbox').style.display='flex'">
    <img src="../../images/moedim-calendar.jpg" alt="Biblical Calendar showing the Hebrew months, agricultural seasons, and feast days" style="width: 100%; max-width: 800px; border-radius: 10px; box-shadow: 0 4px 16px rgba(0,0,0,0.12);">
    <div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(30,58,79,0.7) 0%, transparent 60%); border-radius: 0 0 10px 10px; padding: 12px; text-align: center;">
      <span style="color: white; font-size: 0.8em; opacity: 0.9;">Tap to enlarge</span>
    </div>
  </div>
  <p style="font-size: 0.8em; color: var(--text-muted); margin-top: 8px; font-style: italic;">The Hebrew calendar with agricultural seasons and appointed times.</p>
</div>

<!-- Calendar Lightbox -->
<div id="calendar-lightbox" onclick="this.style.display='none'" style="display:none; position:fixed; inset:0; z-index:9999; background:rgba(0,0,0,0.92); flex-direction:column; align-items:center; justify-content:center; cursor:zoom-out; padding:20px;">
  <div style="color:white; font-size:0.85em; margin-bottom:10px; opacity:0.7;">Tap anywhere to close</div>
  <div style="overflow:auto; max-width:95vw; max-height:85vh; -webkit-overflow-scrolling:touch;" onclick="event.stopPropagation()">
    <img src="../../images/moedim-calendar-full.png" alt="Biblical Calendar — full resolution" style="max-width: none; width: 3840px; display:block; background: white; border-radius: 8px; padding: 20px;">
  </div>
</div>

<div id="feast-countdown" style="background: linear-gradient(135deg, #1e3a4f 0%, #2a4f6a 100%); border-radius: 12px; padding: 28px 32px; margin: 30px 0; color: white; text-align: center;">
  <div style="font-size: 0.8em; text-transform: uppercase; letter-spacing: 2px; opacity: 0.7; margin-bottom: 6px;">Next Appointed Time</div>
  <div id="feast-name" style="font-family: Georgia, serif; font-size: 1.6em; margin-bottom: 2px; color: #d5a93c;"></div>
  <div id="feast-hebrew" style="font-family: Georgia, serif; font-size: 1.1em; opacity: 0.8; margin-bottom: 4px;"></div>
  <div id="feast-hdate" style="font-size: 0.9em; opacity: 0.7; margin-bottom: 4px;"></div>
  <div id="feast-date" style="font-size: 0.85em; opacity: 0.5; margin-bottom: 16px;"></div>
  <div id="feast-timer" style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;"></div>
  <div id="feast-desc" style="font-size: 0.85em; opacity: 0.7; margin-top: 16px; max-width: 600px; margin-left: auto; margin-right: auto; line-height: 1.6;"></div>
</div>

<script>
(function() {
  var feasts = [
    { name: "Purim", hebrew: "פורים", hdate: "14 Adar 5786", date: "2026-03-03", desc: "Celebration of deliverance as told in the Book of Esther." },
    { name: "Pesach (Passover)", hebrew: "פסח", hdate: "15 Nisan 5786", date: "2026-04-02", desc: "The Feast of Unleavened Bread — commemorating the Exodus and freedom from Egypt. The lamb's blood on the doorposts points to Christ, the Lamb of God." },
    { name: "Shavuot (Pentecost)", hebrew: "שבועות", hdate: "6 Sivan 5786", date: "2026-05-22", desc: "The Feast of Weeks — 50 days after Passover. Commemorates the giving of the Torah at Sinai. The Holy Spirit was poured out on Pentecost (Acts 2)." },
    { name: "Rosh Hashanah", hebrew: "ראש השנה", hdate: "1 Tishri 5787", date: "2026-09-12", desc: "The Day of Trumpets — the shofar blast calls God's people to repentance and points toward the Second Coming." },
    { name: "Yom Kippur", hebrew: "יום כיפור", hdate: "10 Tishri 5787", date: "2026-09-21", desc: "The Day of Atonement — the holiest day, when the High Priest entered the Holy of Holies. Points to final judgment and reconciliation." },
    { name: "Sukkot (Tabernacles)", hebrew: "סוכות", hdate: "15 Tishri 5787", date: "2026-09-26", desc: "The Feast of Tabernacles — dwelling in temporary shelters, remembering the wilderness. Points to the Millennium — God tabernacling with His people." },
    { name: "Hanukkah", hebrew: "חנוכה", hdate: "25 Kislev 5787", date: "2026-12-05", desc: "The Festival of Lights — celebrating the rededication of the Second Temple and the miracle of the oil." },
    { name: "Purim", hebrew: "פורים", hdate: "14 Adar 5787", date: "2027-03-24", desc: "Celebration of deliverance as told in the Book of Esther." },
    { name: "Pesach (Passover)", hebrew: "פסח", hdate: "15 Nisan 5787", date: "2027-04-22", desc: "The Feast of Unleavened Bread — commemorating the Exodus and freedom from Egypt." }
  ];

  function update() {
    var now = new Date();
    var next = null;
    for (var i = 0; i < feasts.length; i++) {
      var d = new Date(feasts[i].date + "T00:00:00");
      if (d > now) { next = feasts[i]; next._date = d; break; }
    }
    if (!next) return;

    document.getElementById("feast-name").textContent = next.name;
    document.getElementById("feast-hebrew").textContent = next.hebrew;
    document.getElementById("feast-hdate").textContent = next.hdate;
    document.getElementById("feast-date").textContent = next._date.toLocaleDateString("en-US", { weekday: "long", year: "numeric", month: "long", day: "numeric" });
    document.getElementById("feast-desc").textContent = next.desc;

    var diff = next._date - now;
    var days = Math.floor(diff / 86400000);
    var hours = Math.floor((diff % 86400000) / 3600000);
    var mins = Math.floor((diff % 3600000) / 60000);
    var secs = Math.floor((diff % 60000) / 1000);

    document.getElementById("feast-timer").innerHTML =
      '<div><div style="font-size:2em;font-weight:700;">' + days + '</div><div style="font-size:0.7em;text-transform:uppercase;letter-spacing:1px;opacity:0.6;">Days</div></div>' +
      '<div><div style="font-size:2em;font-weight:700;">' + hours + '</div><div style="font-size:0.7em;text-transform:uppercase;letter-spacing:1px;opacity:0.6;">Hours</div></div>' +
      '<div><div style="font-size:2em;font-weight:700;">' + mins + '</div><div style="font-size:0.7em;text-transform:uppercase;letter-spacing:1px;opacity:0.6;">Minutes</div></div>' +
      '<div><div style="font-size:2em;font-weight:700;">' + secs + '</div><div style="font-size:0.7em;text-transform:uppercase;letter-spacing:1px;opacity:0.6;">Seconds</div></div>';
  }

  update();
  setInterval(update, 1000);
})();
</script>

### The Seven Moedim at a Glance

The Hebrew word **מועדים** (*moedim*) means "appointed times" — divine appointments woven into creation itself (Genesis 1:14). The seven feasts of Leviticus 23 trace God's redemptive plan:

<div style="margin: 24px 0;">

<div style="margin-bottom: 8px; padding: 8px 16px; background: linear-gradient(135deg, #4a6b52 0%, #5a7d62 100%); color: white; border-radius: 8px 8px 0 0; font-family: Georgia, serif; font-size: 0.95em; letter-spacing: 0.5px;">Spring Feasts — Fulfilled in Christ</div>

<div style="display: grid; grid-template-columns: 1fr; gap: 0; margin-bottom: 20px;">

<div style="display: flex; align-items: center; padding: 14px 18px; background: #f7f9f7; border-left: 4px solid #4a6b52; border-bottom: 1px solid #e8ede9;">
  <div style="flex: 1;">
    <div style="font-weight: 700; color: #1e3a4f; font-size: 1.05em;">Passover</div>
    <div style="font-size: 0.85em; color: #57899c;">Pesach · פסח</div>
  </div>
  <div style="text-align: right;">
    <div style="font-weight: 600; color: #1e3a4f;">April 2</div>
    <div style="font-size: 0.8em; color: #57899c;">15 Nisan</div>
  </div>
</div>

<div style="display: flex; align-items: center; padding: 14px 18px; background: white; border-left: 4px solid #4a6b52; border-bottom: 1px solid #e8ede9;">
  <div style="flex: 1;">
    <div style="font-weight: 700; color: #1e3a4f; font-size: 1.05em;">Unleavened Bread</div>
    <div style="font-size: 0.85em; color: #57899c;">Matzot · מצות</div>
  </div>
  <div style="text-align: right;">
    <div style="font-weight: 600; color: #1e3a4f;">April 2–9</div>
    <div style="font-size: 0.8em; color: #57899c;">15–22 Nisan</div>
  </div>
</div>

<div style="display: flex; align-items: center; padding: 14px 18px; background: #f7f9f7; border-left: 4px solid #4a6b52; border-bottom: 1px solid #e8ede9;">
  <div style="flex: 1;">
    <div style="font-weight: 700; color: #1e3a4f; font-size: 1.05em;">Firstfruits</div>
    <div style="font-size: 0.85em; color: #57899c;">Bikkurim · ביכורים</div>
  </div>
  <div style="text-align: right;">
    <div style="font-weight: 600; color: #1e3a4f;">April 5</div>
    <div style="font-size: 0.8em; color: #57899c;">18 Nisan</div>
  </div>
</div>

<div style="display: flex; align-items: center; padding: 14px 18px; background: white; border-left: 4px solid #4a6b52; border-radius: 0 0 8px 0;">
  <div style="flex: 1;">
    <div style="font-weight: 700; color: #1e3a4f; font-size: 1.05em;">Pentecost</div>
    <div style="font-size: 0.85em; color: #57899c;">Shavuot · שבועות</div>
  </div>
  <div style="text-align: right;">
    <div style="font-weight: 600; color: #1e3a4f;">May 22</div>
    <div style="font-size: 0.8em; color: #57899c;">6 Sivan</div>
  </div>
</div>

</div>

<div style="margin-bottom: 8px; padding: 8px 16px; background: linear-gradient(135deg, #1e3a4f 0%, #2a4f6a 100%); color: white; border-radius: 8px 8px 0 0; font-family: Georgia, serif; font-size: 0.95em; letter-spacing: 0.5px;">Fall Feasts — Yet to Be Fulfilled</div>

<div style="display: grid; grid-template-columns: 1fr; gap: 0;">

<div style="display: flex; align-items: center; padding: 14px 18px; background: #f5f7fa; border-left: 4px solid #1e3a4f; border-bottom: 1px solid #e0e5ea;">
  <div style="flex: 1;">
    <div style="font-weight: 700; color: #1e3a4f; font-size: 1.05em;">Trumpets</div>
    <div style="font-size: 0.85em; color: #57899c;">Yom Teruah · יום תרועה</div>
  </div>
  <div style="text-align: right;">
    <div style="font-weight: 600; color: #1e3a4f;">Sept 12</div>
    <div style="font-size: 0.8em; color: #57899c;">1 Tishri</div>
  </div>
</div>

<div style="display: flex; align-items: center; padding: 14px 18px; background: white; border-left: 4px solid #1e3a4f; border-bottom: 1px solid #e0e5ea;">
  <div style="flex: 1;">
    <div style="font-weight: 700; color: #1e3a4f; font-size: 1.05em;">Atonement</div>
    <div style="font-size: 0.85em; color: #57899c;">Yom Kippur · יום כיפור</div>
  </div>
  <div style="text-align: right;">
    <div style="font-weight: 600; color: #1e3a4f;">Sept 21</div>
    <div style="font-size: 0.8em; color: #57899c;">10 Tishri</div>
  </div>
</div>

<div style="display: flex; align-items: center; padding: 14px 18px; background: #f5f7fa; border-left: 4px solid #1e3a4f; border-radius: 0 0 8px 0;">
  <div style="flex: 1;">
    <div style="font-weight: 700; color: #1e3a4f; font-size: 1.05em;">Tabernacles</div>
    <div style="font-size: 0.85em; color: #57899c;">Sukkot · סוכות</div>
  </div>
  <div style="text-align: right;">
    <div style="font-weight: 600; color: #1e3a4f;">Sept 26</div>
    <div style="font-size: 0.8em; color: #57899c;">15 Tishri</div>
  </div>
</div>

</div>
</div>

<p style="font-style: italic; color: var(--text-muted); font-size: 0.9em;">More detailed feast day studies are coming soon.</p>

### Resources

- **[Chabad.org — Jewish Holidays](https://www.chabad.org/holidays/default_cdo/jewish/holidays.htm)** — Authoritative Jewish perspective on each feast's observance and meaning
- **[Hebrew for Christians — The Feasts](https://www.hebrew4christians.com/Holidays/holidays.html)** — Each feast with Hebrew vocabulary and Christ-centered application
- **[My Jewish Learning — Holidays](https://www.myjewishlearning.com/article/jewish-holidays/)** — Accessible overview of the Jewish calendar year

---

## Ancient Israelite Culture

Understanding the daily life, social structures, and worldview of ancient Israel illuminates countless passages that otherwise feel distant or confusing.

### Daily Life & Archaeology

- **[Bible Project — Cultural Context Videos](https://bibleproject.com/)** — Beautifully animated videos exploring themes, word studies, and cultural context throughout the Bible
- **[Biblical Archaeology Society](https://www.biblicalarchaeology.org/)** — The leading popular publication connecting archaeological discoveries to biblical texts. Their free *Bible History Daily* newsletter is excellent.
- **[Ten Minute Bible Hour](https://www.youtube.com/@TheTenMinuteBibleHour)** — Matt Baker's accessible explorations of biblical history, denominations, and context

### Jewish Traditions & Commentary

- **[Chabad.org — Torah & Mitzvot](https://www.chabad.org/library/article_cdo/aid/1426382/jewish/Torah.htm)** — Gateway to Jewish law, custom, and Torah commentary, including Rashi's classic verse-by-verse commentary
- **[My Jewish Learning](https://www.myjewishlearning.com/)** — Accessible articles on Jewish practice, belief, history, and culture
- **[Sefaria](https://www.sefaria.org/)** — Free digital library of Jewish texts — Torah, Mishnah, Talmud, Midrash, commentaries — all interconnected and searchable

---

## BYU & LDS Scholarly Resources

Latter-day Saint scholars have produced exceptional work on biblical context, parables, and ancient Near Eastern culture. These peer-reviewed and faith-affirming resources bring academic rigor to gospel study.

### BYU Religious Studies Center

The [Religious Studies Center](https://rsc.byu.edu/) publishes scholarly articles, books, and the *Religious Educator* journal.

**Parables & Teaching:**
- **[The Savior's Questions: Teachings from the Last Week](https://rsc.byu.edu/vol-10-no-2-2009/saviors-questions-teachings-last-week-his-life)** — Rick B. Jorgensen on Christ's teaching methods during Holy Week
- **[Names of the Parables](https://rsc.byu.edu/vol-4-no-1-2003/names-parables)** — Thomas A. Wayment on how parable titles shape interpretation
- **[Revealing Parables: A Call to Action](https://rsc.byu.edu/you-shall-have-my-word/revealing-parables-call-action-within-doctrine-covenants)** — Amy Easton-Flake on parables in the Doctrine & Covenants
- **[The Great Commandment: Principle or Platitude?](https://rsc.byu.edu/vol-3-no-1-2002/great-commandment-principle-platitude)** — Howard A. Christy on love as active discipleship

**Olivet Discourse & Last Week:**
- **[Discipleship in the Olivet Discourse](https://rsc.byu.edu/behold-lamb-god/discipleship-olivet-discourse-marks-gospel)** — Gaye Strathearn on Mark 13 and watchfulness

### Neal A. Maxwell Institute

The [Maxwell Institute](https://mi.byu.edu/) produces scholarly work on scripture, religion, and the ancient world.

- **[Maxwell Institute Podcast](https://mi.byu.edu/maxwell-institute-podcast-series/)** — In-depth conversations with scholars on scripture and faith
- **[Podcast #28: Parables with Amy-Jill Levine](https://mi.byu.edu/podcast-new-section/28-the-parables-of-jesus-with-amy-jill-levine-mipodcast)** — Jewish scholar perspective on Jesus' parables

### Scripture Central

[Scripture Central](https://scripturecentral.org/) provides free scholarly resources on the Bible and Book of Mormon.

- **[KnoWhy Articles](https://scripturecentral.org/archive/knowhy)** — Brief scholarly insights on specific scripture passages
- **[Ten Virgins KnoWhy](https://scripturecentral.org/knowhy/how-does-the-parable-of-the-ten-virgins-offer-us-direction-in-life)** — Parable of the Ten Virgins explained
- **[Counting to Ten](https://scripturecentral.org/archive/periodicals/journal-article/counting-ten)** — John W. Welch on symbolic numbers in scripture

### Other LDS Academic Sources

- **[BYU Studies](https://byustudies.byu.edu/)** — Scholarly journal on LDS history, scripture, and theology
- **[Interpreter Foundation](https://journal.interpreterfoundation.org/)** — Peer-reviewed journal on scripture and LDS topics
- **[Book of Mormon Central](https://bookofmormoncentral.org/)** — Scholarly resources on the Book of Mormon
