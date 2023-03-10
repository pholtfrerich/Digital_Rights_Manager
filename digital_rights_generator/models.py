from fpdf import FPDF
from django.http import  HttpResponse


# Create your models here.

def generate_pdf(form_data):
    #link = form_data['link']
    licensor = form_data['licensor']
    content_title = form_data['content_title']

    creator = 'Paul Holtfrerich'
    licensing_platform = 'Watermark'
    
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    
    # Set the margins to .5 inches
    margin = .5*25.4
    pdf.set_margins(margin, margin)
    pdf.set_auto_page_break(auto=True, margin=margin)
    pdf.add_page()

    # Add the title
    pdf.set_font('arial', 'B', 18)
    pdf.cell(0, 10, '{} Standard Content License Agreement'.format(licensing_platform), 0, 1, 'C')
    
    # Add body
    pdf.set_font('arial', '', 12)
    agreement_text = f'''

        This AGREEMENT (the “Agreement”) between you ("{licensor}") and creator of the content ("{creator}") that you have selected to access (“Licensor”) governs your use of the Licensor content ("{content_title}") identified in your order (the “Content”). By copying or downloading content from Licensor through the content licensing platform provided by "{licensing_platform}", you accept the terms of this Agreement. If you do not agree with the terms of this Agreement, you may not copy or download the Content. You and Licensor each hereby agree as follows: 

        1. Content License; Ownership. Subject to the terms and conditions of this Agreement, Licensor hereby grants to you a non-exclusive, perpetual, non-transferable, non- sublicensable license, solely to reproduce, perform publicly, display, transmit, and distribute the Content in all media solely for the purposes set forth herein. Licensor reserves all rights not expressly granted to you under this Agreement. Except for the licenses expressly granted to you in this Agreement, you acknowledge that all right, title, and interest in and to the Content is controlled by Licensor. 

        2. Usage of the Content. Notwithstanding any other provision to the contrary contained in this Agreement: 

            2.1 Permitted Uses. Subject to the terms and conditions herein, you may use the Content on websites, social media, marketing materials, presentations, educational works, editorial works, audiovisual works, literary works, and product packaging. 

            2.2 Copyright Notices. You shall ensure that your use of the Content is marked with the appropriate copyright notices specified by Licensor. 

            2.3 Attribution. You will use commercially reasonable efforts to include attribution for Licensor in accordance with industry standards, including without limitation, in any editorial or audiovisual works. 

            2.4 Restrictions. The following restrictions apply to your use of the Content: 
                (a) You shall not use the Content in a pornographic, defamatory, obscene, or otherwise unlawful manner; 
                (b) You shall not use the Content as part of a trademark, service mark, trade dress, logo or other source identifying asset; 
                (c) You shall not use the Content in a way that allows others to download, extract, or redistribute the Content as a standalone file; 
                (d) You shall not use the Content with material that violates any third-party rights, or otherwise take any action in connection with the Content that violates the rights of others; 
                (e) You shall not use the Content other than for your own benefit or for the benefit of a single company/client without additional licenses; 
                (f) You shall not falsely represent that you are the original creator of the Content; 
                (g) You shall not use the Content in connection with any goods or services intended for resale or distribution where the primary value of such goods or services is in the Content itself including, without limitation, cards, stationery items, paper products, calendars, apparel items, posters, DVDs, mobile applications or other items for resale, on-demand merchandise printing, license or other distribution for profit. 

            2.5 Modifications. You may adapt the Content (for example, resizing, minor cropping, embedding) for your intended use, however you shall modify the creative expression of the 
            Content or create any derivative works of the Content without Licensor’s express prior written permission. 

        3. Payment. As consideration in full for the rights granted herein, you shall pay Licensor the one-time fee ("$1000") identified in the order using the {licensing_platform} platform, prior to downloading or copying the Content. 

        4. Company Use. If you are licensing the Content on behalf of your employer or company, you hereby: (a) represent and warrant that you have the full legal authority to bind your employer or company; (b) agree that you remain responsible for the use of the Content by your employer or company; (c) agree that the entity that uses the Content agrees to be bound by the terms of this Agreement; and (d) agree to purchase additional licenses of the same Content if it is used by or for multiple entities. 

        5. Protection of the Content. You shall immediately notify {licensing_platform} of any: (a) actual, suspected, or threatened infringement of the Content; (b) actual, suspected, or threatened claim that use of the Content infringes the rights of any third party; or (c) any other actual, suspected, or threatened claim to which the Content may be subject. With respect to any of the matters listed in this Section as between you and Licensor: (i) Licensor has exclusive control over, and conduct of, all claims and proceedings; (ii) you shall provide Licensor with all assistance that Licensor may reasonably require; and (iii) Licensor shall bear the cost of any proceedings and will be entitled to retain all sums recovered in any action. Licensor or {licensing_platform} may discontinue licensing any piece of Content at any time in its sole discretion. Upon notice from {licensing_platform} that any content may be subject to a claim of infringement of a third party’s right, {licensing_platform} may require you to immediately, and at your own expense, cease using the Content and delete any copies. 

        6. Representations and Warranties. 
            
            6.1 Licensors Representations and Warranties. Licensor represents and warrants, solely to and for your benefit, that it has the right to license the Content in connection with your uses permitted hereunder. 
            
            6.2 Your Representations and Warranties. You represent and warrant that: 
                (a) You will not engage or participate in any activity or course of action that could diminish or tarnish the image or reputation of the Content, Licensor, or {licensing_platform}, or cause confusion as to the ownership of the Content; and 
                (b) Your use of the Content will not infringe, misappropriate, or otherwise violate the intellectual property or other rights of any third party or violate any applicable regulation or law. 

            6.3 Disclaimer of Representations and Warranties. EXCEPT AS EXPRESSLY PROVIDED IN THIS SECTION 6, LICENSOR AND {licensing_platform} EACH EXPRESSLY DISCLAIMS ALL WARRANTIES, WHETHER EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE, WITH RESPECT TO THE LICENSED PROPERTY, INCLUDING ANY IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, NON-INFRINGEMENT, AND WARRANTIES THAT MAY ARISE OUT OF COURSE OF DEALING, COURSE OF PERFORMANCE, USAGE, OR TRADE PRACTICE. 

        7. Term and Termination.
            
            7.1 Term. This Agreement is effective until it is terminated by either party (the “Term”). 
            
            7.2 Termination for Breach. Licensor may terminate this Agreement at any time if you 
        breach the terms of this Agreement. Upon such termination you shall immediately stop 
        using the Content, delete or destroy any copies and confirm to License in writing that you have complied with this Section. 
            
            7.3 Termination by You. You may terminate this Agreement by ceasing to use the Content and deleting or destroying any copies. 

        7.4 Termination for Third Party Use. If your use of the Content becomes subject to use by a social media platform or other third-party website for its own purpose, this Agreement shall immediately terminate and you will remove the Content from such site. 

        7.5 Effect of Termination. Upon the expiration or termination of this Agreement for any reason, all rights licensed under this Agreement will revert immediately to Licensor and you shall cause to be inactivated and erased all digital copies of the Content in your control and possession and return or, at Licensor’s written request, destroy, any tangible copies of the Content. Any rights or obligations of the parties in this Agreement which, by their nature, should survive termination or expiration of this Agreement will survive any such termination or expiration. 

        8. Remedies. 

            8.1 Equitable Relief. You acknowledge your breach of this Agreement may cause {licensing_platform} and Licensor irreparable damages, for which an award of damages would not be adequate compensation, and agree that, in the event of such breach or threatened breach, Licensor or {licensing_platform} will be entitled to seek equitable relief, including injunctive relief, in addition to any other remedy to which Licensor or {licensing_platform} may be entitled at law or in equity. Such remedies are not exclusive but are in addition to all other remedies available at law or in equity. 

            8.2 Limitation of Liability. {licensing_platform} AND LICENSOR WILL NOT BE LIABLE UNDER OR IN CONNECTION WITH THIS AGREEMENT FOR INDIRECT, INCIDENTAL, CONSEQUENTIAL, LIQUIDATED, SPECIAL, OR EXEMPLARY DAMAGES OR PENALTIES, INCLUDING LOSSES OF BUSINESS, REVENUE, OR ANTICIPATED PROFITS, REGARDLESS OF WHETHER SUCH DAMAGE WAS FORESEEABLE AND WHETHER {licensing_platform} OR ITS LICENSORS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. {licensing_platform}’S AND LICENSOR’S TOTAL MAXIMUM AGGREGATE LIABILITY UNDER THIS AGREEMENT WILL IN NO EVENT EXCEED ,000. NOTWITHSTANDING ANY OTHERWISE APPLICABLE STATUTE OF LIMITATIONS, ANY ACTION OR DISPUTE RESOLUTION PROCEEDING MUST BE COMMENCED WITHIN TWO YEARS OF THE ACT, EVENT, OR OCCURRENCE GIVING RISE TO THE CLAIM. THE FOREGOING DOES NOT AFFECT ANY LIABILITY OR CLAIM WHICH CANNOT BE EXCLUDED OR LIMITED UNDER APPLICABLE LAW. 

        9. General. 

            9.1 Entire Agreement; Amendment. This Agreement, including and together with any related attachments, constitutes the sole and entire agreement of the parties with respect to the subject matter contained herein. No amendment or modification to this Agreement is effective unless it is in writing and signed by an authorized representative of each party. 

            9.2 Severability. If any term or provision of this Agreement is invalid, illegal, or unenforceable in any jurisdiction, such invalidity, illegality, or unenforceability will not affect the enforceability of any other term or provision of this Agreement, or invalidate or render unenforceable such term or provision in any other jurisdiction. 

            9.3 Assignment. You shall not assign any of its rights or delegate any of its obligations under this Agreement without the prior written consent of Licensor. Any purported 
            assignment or delegation in violation of this Section 9.3 is null and void. Licensor may freely assign or otherwise transfer any of its rights or delegate any of its obligations under this Agreement. This Agreement is binding upon and inures to the benefit of the parties hereto and their respective permitted successors and assigns. 

            9.4 Choice of Law; Venue. This Agreement and all matters arising out of or relating to this Agreement are governed by the laws of Texas, without giving effect to any conflict of laws provisions thereof that would result in the application of the laws of a different jurisdiction. Either party shall institute any legal suit, action, or proceeding arising out of or relating to this Agreement in the federal or state courts in each case located in Dallas, Texas, and each party irrevocably submits to the exclusive jurisdiction of such courts in any legal suit, action, or proceeding. 

            9.5 Relationship of the Parties. The relationship between the parties is that of independent contractors. Nothing contained in this Agreement will be construed as creating any agency, partnership, joint venture, or other form of joint enterprise, employment, or fiduciary relationship between the parties, and neither party has authority to contract for or bind the other party in any manner whatsoever. 

            9.6 Third Party Beneficiaries. Except as set forth in this Section 9.6, the parties do not confer any rights or remedies up on any person other than the parties to this Agreement and their respective successors and permitted assigns. Notwithstanding the foregoing, the parties hereby designate {licensing_platform} as a third-party beneficiary of this Agreement having the right to enforce the terms and conditions herein. 

            9.7 Waiver. No waiver by any party of any of the provisions hereof will be effective unless explicitly set forth in writing and signed by the party so waiving. Except as otherwise set forth in this Agreement, no failure to exercise, or delay in exercising, any right, remedy, power, or privilege arising from this Agreement will operate or be construed as a waiver thereof; nor will any single or partial exercise of any right, remedy, power, or privilege hereunder preclude any other or further exercise thereof, or the exercise of any other right, remedy, power, or privilege. 
        '''
    agreement_text = agreement_text.encode('ascii', 'ignore').decode()
    pdf.multi_cell(0, 10, agreement_text)
    
    # Get the PDF content as a bytes object
    pdf_content = pdf.output(dest='S').encode('latin1')

    # Create a HttpResponse with the PDF content
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="agreement.pdf"'
    return response