Markdown ���
==================

![Markdown](https://markdown.tw/images/208x128.png)

**NOTE:** This is Traditional Chinese Edition Document of
Markdown Syntax. If you are seeking for English Edition 
Document. Please refer to [Markdown: Syntax][eng-doc].

[eng-doc]:http://daringfireball.net/projects/markdown/syntax

Markdown: Syntax
================

*   [���z](#overview)
    *   [����](#philosophy)
    *   [�椺 HTML](#html)
    *   [�S��r���۰��ഫ](#autoescape)
*   [�϶�����](#block)
    *   [�q���M����](#p)
    *   [���D](#header)
    *   [�϶��ި�](#blockquote)
    *   [�M��](#list)
    *   [�{���X�϶�](#precode)
    *   [���j�u](#hr)
*   [�Ϭq����](#span)
    *   [�s��](#link)
    *   [�j��](#em)
    *   [�{���X](#code)
    *   [�Ϥ�](#img)
*   [�䥦](#misc)
    *   [����r��](#backslash)
    *   [�۰ʳs��](#autolink)
*   [�P��](#acknowledgement)

**�`�N�G**�o�����O�� Markdown �g���A�A�i�H[�ݬݥ�����l��][src] �C

  [src]: https://github.com/othree/markdown-syntax-zhtw/blob/master/syntax.md

* * *

<h2 id="overview">���z</h2>

<h3 id="philosophy">����</h3>

Markdown ���ؼЬO��{�u��Ū���g�v�C

���L�̻ݭn�j�ժ��K�O�����iŪ�ʡC�@���ϥ� Markdown �榡���g��������ӥi�H�����H�¤�r�o�G�A�åB�ݰ_�Ӥ��|���O�ѳ\�h���ҩάO�榡���O�Һc���CMarkdown �y�k����@�ǬJ�� text-to-HTML �榡���v�T�A�]�A [Setext] [1]�B[atx] [2]�B[Textile] [3]�B[reStructuredText] [4]�B[Grutatext] [5] �M [EtText] [6]�A�M�ӳ̤j�F�P�ӷ����O�¤�r���q�l�l��榡�C

  [1]: http://docutils.sourceforge.net/mirror/setext.html
  [2]: http://www.aaronsw.com/2002/atx/
  [3]: http://textism.com/tools/textile/
  [4]: http://docutils.sourceforge.net/rst.html
  [5]: http://www.triptico.com/software/grutatxt.html
  [6]: http://ettext.taint.org/doc/

�]�� Markdown ���y�k���Ѽ��I�Ÿ��Ҳզ��A�øg�L�Y�ԷV��A�O���F�����̬ݰ_�ӴN���ҭn��F���N��C���O�b��r��ǥ[�W�P���A�ݰ_�ӴN��\*�j��\*�CMarkdown ���M��ݰ_�ӡA��A�N�O�M��C���p�A���ϥιL�q�l�l��A�϶��ި��ݰ_�ӴN�u�����O�ޥΤ@�q��r�C

<h3 id="html">�椺 HTML</h3>

Markdown ���y�k���ӥD�n���ت��G�Ψӧ@���@�غ������e��*�g�@*�λy���C

Markdown ���O�n�Ө��N HTML�A�Ʀܤ]�S���n�M���ۦ��A�����y�k�������h�A�u�M HTML ���@���������Y�A���I*���O*�n�гy�@�ا�e���g�@ HTML ��󪺻y�k�A�ڻ{�� HTML �w�g�ܮe���g�F�AMarkdown �����I�b��A����������e���\Ū�B�s�g�CHTML �O�@��*�o�G*���榡�AMarkdown �O�@��*�s�g*���榡�A�]���AMarkdown ���榡�y�k�u�[�\�¤�r�i�H�[�\���d��C

���b Markdown �[�\�d�򤧥~�����ҡA���i�H�����b���̭��� HTML ���g�C���ݭn�B�~�е��o�O HTML �άO Markdown�F�u�n�����[���ҴN�i�H�F�C

�u���϶������w�w��p `<div>`�B`<table>`�B`<pre>`�B`<p>` �����ҡA�����b�e��[�W�Ŧ�A�H�Q�P���e�Ϲj�C�ӥB�o�ǡ]�����^���}�l�P�������ҡA���i�H�� tab �άO�ťը��Y�ơCMarkdown �����;������z���P�_�A�i�H�קK�b�϶����ҫe��[�W�S�����n�� `<p>` ���ҡC

�|�Ҩӻ��A�b Markdown ���̥[�W�@�q HTML ���G

    This is a regular paragraph.

    <table>
        <tr>
            <td>Foo</td>
        </tr>
    </table>

    This is another regular paragraph.

�Ъ`�N�AMarkdown �y�k�b HTML �϶����Ҥ��N���|�Q�i��B�z�C�Ҧp�A�A�L�k�b HTML �϶����ϥ� Markdown �Φ���`*�j��*`�C

HTML ���Ϭq���Ҧp `<span>`�B`<cite>`�B`<del>` �h��������A�i�H�b Markdown ���q���B�M��άO���D�̥��N�ϥΡC�̷ӭӤH�ߺD�A�Ʀܥi�H����Markdown �榡�A�ӱĥ� HTML ���ҨӮ榡�ơC�|�һ����G�p�G������w HTML ��  `<a>` �� `<img>` ���ҡA�i�H�����ϥγo�Ǽ��ҡA�Ӥ��� Markdown ���Ѫ��s���άO�v���Хܻy�k�C

HTML �Ϭq���ҩM�϶����Ҥ��P�A�b�Ϭq���Ҫ��d�򤺡A Markdown ���y�k�O���Ī��C

<h3 id="autoescape">�S��r���۰��ഫ</h3>

�b HTML ��󤤡A����Ӧr���ݭn�S��B�z�G `<` �M `&` �C `<` �Ÿ��Ω�_�l���ҡA`&` �Ÿ��h�Ω�аO HTML ����A�p�G�A�u�O�Q�n�ϥγo�ǲŸ��A�A�����n�ϥι��骺�Φ��A���O `&lt;` �M `&amp;`�C

`&` �Ÿ����ܮe�����g�@������󪺤H�P��x�Z�A�p�G�A�n���uAT&T�v �A�A�����n�g���u`AT&amp;T`�v �A�ٱo�ഫ���}���� `&` �Ÿ��A�p�G�A�n�s����G

    http://images.google.com/images?num=30&q=larry+bird

�A�����n����}�ন�G

    http://images.google.com/images?num=30&amp;q=larry+bird

�~����s�����Ҫ� `href` �ݩʸ̡C���λ��]���D�o�ܮe���ѰO�A�o�]�i��O HTML �з��ˬd���ˬd�쪺���~���A�ƶq�̦h���C

Markdown ���\�A�����ϥγo�ǲŸ��A���O�A�n�p�߸���r�����ϥΡA�p�G�A�O�bHTML ���餤�ϥ� `&` �Ÿ����ܡA�����|�Q�ഫ�A�Ӧb�䥦���ΤU�A���h�|�Q�ഫ�� `&amp;`�C�ҥH�A�p�G�n�b��󤤴��J�@�ӵۧ@�v���Ÿ��A�A�i�H�o�˼g�G

    &copy;

Markdown �N���|��o�q��r���ק�A���O�p�G�A�o�˼g�G

    AT&T

Markdown �N�|�N���ର�G

    AT&amp;T

���������p�]�|�o�ͦb `<` �Ÿ��W�A�]�� Markdown �䴩 [�椺 HTML](#html) �A�p�G�A�O�ϥ� `<` �Ÿ��@�� HTML ���ҨϥΡA�� Markdown �]���|�復�������ഫ�A���O�p�G�A�O�g�G

    4 < 5

Markdown �N�|�⥦�ഫ���G

    4 &lt; 5

���L�ݭn�`�N���O�Acode �d�򤺡A���׬O�椺�٬O�϶��A `<` �M `&` ��ӲŸ���*�@�w*�|�Q�ഫ�� HTML ����A�o���S�����A�i�H�ܮe���a�� Markdown �g HTML code �]�M HTML �۹�Ө��A HTML �y�k���A�A�n��Ҧ��� `<` �M `&` ���ഫ�� HTML ����A�~��b HTML ���̭��g�X HTML code�C�^

* * *

<h2 id="block">�϶�����</h2>


<h3 id="p">�q���M����</h3>

�@�Ӭq���O�Ѥ@�ӥH�W�۳s������y�զ��A�Ӥ@�ӥH�W���Ŧ�h�|�����X���P���q���]�Ŧ檺�w�q�O��ܤW�ݰ_�ӹ��O�Ŧ�A�K�|�Q�����Ŧ�C��軡�A�Y�Y�@��u�]�t�ťթM tab�A�h�Ӧ�]�|�Q�����Ŧ�^�A�@�몺�q�����ݭn�Ϊťթ��_���Y�ơC

�u�@�ӥH�W�۳s������y�զ��v�o�y�ܨ��t�ܤF Markdown ���\�q�������j���_��A�o�ӯS�ʩM��L�j������ text-to-HTML �榡���@�ˡ]�]�A MovableType ���uConvert Line Breaks�v�ﶵ�^�A�䥦���榡�|��C���_�泣�ন `<br />` ���ҡC

�p�G�A*�u��*�Q�n���J `<br />` ���Ҫ��ܡA�b����[�W��ӥH�W���ťաA�M��� enter�C

�O���A�o�T��ݭn�����h�\�ҨӴ��J `<br />` �A���O�u�C�Ӵ��泣�ഫ�� `<br />`�v����k�b Markdown ���ä��A�X�A Markdown �� email ���� [�϶��ި�][bq] �M�h�q���� [�M��][l] �b�ϥδ���ӱƪ����ɭԡA������n�ΡA�٧�n�\Ū�C

  [bq]: #blockquote
  [l]:  #list

<h3 id="header">���D</h3>

Markdown �䴩��ؼ��D���y�k�A[Setext] [1] �M [atx] [2] �Φ��C

Setext �Φ��O�Ω��u���Φ��A�Q�� `=` �]�̰������D�^�M `-` �]�ĤG�����D�^�A�Ҧp�G

    This is an H1
    =============

    This is an H2
    -------------

����ƶq�� `=` �M `-` ���i�H���ĪG�C

Atx �Φ��h�O�b�歺���J 1 �� 6 �� `#` �A��������D 1 �� 6 ���A�Ҧp�G

    # This is an H1

    ## This is an H2

    ###### This is an H6

�A�i�H��ܩʦa�u�����vatx �˦������D�A�o�º�u�O���[�Ϊ��A�Y�Oı�o�o�ˬݰ_�Ӥ���ξA�A�A�N�i�H�b����[�W `#`�A�Ӧ���� `#` �ƶq�]���ΩM�}�Y�@�ˡ]�歺�����r�ƶq�M�w���D�����ơ^�G

    # This is an H1 #

    ## This is an H2 ##

    ### This is an H3 ######


<h3 id="blockquote">Blockquotes</h3>

Markdown �ϥ� email �Φ����϶��ި��A�p�G�A�ܼ��x�p��b email �H�󤤤ި��A�A�N���D���b Markdown ��󤤫إߤ@�Ӱ϶��ި��A���|�ݰ_�ӹ��O�A�j���_��A�M��b�C�檺�̫e���[�W `>` �G

    > This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
    > consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
    > Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
    > 
    > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
    > id sem consectetuer libero luctus adipiscing.

Markdown �]���\�A�u�b��Ӭq�����Ĥ@��̫e���[�W `>` �G

    > This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
    consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
    Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

    > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
    id sem consectetuer libero luctus adipiscing.

�϶��ި��i�H�����h�]�Ҧp�G�ި������ި��^�A�u�n�ھڼh�ƥ[�W���P�ƶq�� `>` �G

    > This is the first level of quoting.
    >
    > > This is nested blockquote.
    >
    > Back to the first level.

�ި����϶����]�i�H�ϥΨ�L�� Markdown �y�k�A�]�A���D�B�M��B�{���X�϶����G

	> ## This is a header.
	> 
	> 1.   This is the first list item.
	> 2.   This is the second list item.
	> 
	> Here's some example code:
	> 
	>     return shell_exec("echo $input | $markdown_script");

����зǪ���r�s�边����²��a�إ� email �˦����ި��A�Ҧp BBEdit �A�A�i�H�����r��M��q��椤���*�W�[�ި����h*�C

<h3 id="list">�M��</h3>

Markdown �䴩���ǲM��M�L�ǲM��C

�L�ǲM��ϥάP���B�[���άO��@���M��аO�G

    *   Red
    *   Green
    *   Blue

���P��G

    +   Red
    +   Green
    +   Blue

�]���P��G

    -   Red
    -   Green
    -   Blue

���ǲM��h�ϥμƦr���ۤ@�ӭ^��y�I�G

    1.  Bird
    2.  McHale
    3.  Parish

�ܭ��n���@�I�O�A�A�b�M��аO�W�ϥΪ��Ʀr�ä��|�v�T��X�� HTML ���G�A�W�����M��Ҳ��ͪ� HTML �аO���G

    <ol>
    <li>Bird</li>
    <li>McHale</li>
    <li>Parish</li>
    </ol>

�p�G�A���M��аO�g���G

    1.  Bird
    1.  McHale
    1.  Parish

�άƦܬO�G

    3. Bird
    1. McHale
    8. Parish

�A���|�o�짹���ۦP�� HTML ��X�C���I�b��A�A�i�H�� Markdown ��󪺲M��Ʀr�M��X�����G�ۦP�A�άO�A�i�@�I�A�A�i�H�������Φb�N�Ʀr�����T�ʡC

�p�G�A�ϥ��i�k���g�k�A��ĳ�Ĥ@�Ӷ��س̦n�٬O�q 1. �}�l�A�]�� Markdown ���ӥi��|�䴩���ǲM�檺 start �ݩʡC

�M�涵�ؼаO�q�`�O��b�̥���A���O���]�i�H�Y�ơA�̦h�T�ӪťաA���ؼаO�᭱�h�@�w�n���ۦܤ֤@�Ӫťթ� tab�C

�n���M��ݰ_�ӧ�}�G�A�A�i�H�⤺�e�ΩT�w���Y�ƾ�z�n�G

    *   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
        Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
        viverra nec, fringilla in, laoreet vitae, risus.
    *   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
        Suspendisse id sem consectetuer libero luctus adipiscing.

���O�p�G�A���i�A���]���@�w�ݭn�G

    *   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
    *   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.

�p�G�M�涵�ض��ΪŦ���}�A Markdown �|�ⶵ�ت����e�b��X�ɥ� `<p>` 
���ҥ]�_�ӡA�|�Ҩӻ��G

    *   Bird
    *   Magic

�|�Q�ഫ���G

    <ul>
    <li>Bird</li>
    <li>Magic</li>
    </ul>

���O�o�ӡG

    *   Bird

    *   Magic

�|�Q�ഫ���G

    <ul>
    <li><p>Bird</p></li>
    <li><p>Magic</p></li>
    </ul>

�M�涵�إi�H�]�t�h�Ӭq���A�C�Ӷ��ؤU���q���������Y�� 4 �ӪťթάO�@�� tab �G

    1.  This is a list item with two paragraphs. Lorem ipsum dolor
        sit amet, consectetuer adipiscing elit. Aliquam hendrerit
        mi posuere lectus.

        Vestibulum enim wisi, viverra nec, fringilla in, laoreet
        vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
        sit amet velit.

    2.  Suspendisse id sem consectetuer libero luctus adipiscing.

�p�G�A�C�泣���Y�ơA�ݰ_�ӷ|�ݦn�ܦh�A��M�A�A���a�A�p�G�A���i�k�AMarkdown �]���\�G

    *   This is a list item with two paragraphs.

        This is the second paragraph in the list item. You're
    only required to indent the first line. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit.

    *   Another item in the same list.

�p�G�n�b�M�涵�ؤ���i�ި��A�� `>` �N�ݭn�Y�ơG

    *   A list item with a blockquote:

        > This is a blockquote
        > inside a list item.

�p�G�n��{���X�϶����ܡA�Ӱ϶��N�ݭn�Y��*�⦸*�A�]�N�O 8 �ӪťթάO��� tab�G

    *   A list item with a code block:

            <code goes here>


��M�A���زM��ܥi��|���p�߲��͡A���O�U���o�˪��g�k�G

    1986. What a great season.

���y�ܻ��A�]�N�O�b�歺�X�{*�Ʀr-�y�I-�ť�*�A�n�קK�o�˪����p�A�A�i�H�b�y�I�e���[�W�ϱ׽u�C

    1986\. What a great season.

<h3 id="precode">�{���X�϶�</h3>

�M�{���������g�@�άO���һy����l�X�q�`�|���w�g�ƪ��n���{���X�϶��A�q�`�o�ǰ϶��ڭ̨ä��Ʊ楦�H�@��q����󪺤覡�h�ƪ��A�ӬO�ӭ�Ӫ��ˤl��ܡAMarkdown �|�� `<pre>` �M `<code>` ���Ҩӧ�{���X�϶��]�_�ӡC

�n�b Markdown ���إߵ{���X�϶���²��A�u�n²��a�Y�� 4 �ӪťթάO 1 �� tab �N�i�H�A�Ҧp�A�U������J�G

    This is a normal paragraph:

        This is a code block.

Markdown �|�ഫ���G

    <p>This is a normal paragraph:</p>

    <pre><code>This is a code block.
    </code></pre>

�o�ӨC��@�����Y�ơ]4 �ӪťթάO 1 �� tab�^�A���|�Q�����A�Ҧp�G

    Here is an example of AppleScript:

        tell application "Foo"
            beep
        end tell

�|�Q�ഫ���G

    <p>Here is an example of AppleScript:</p>

    <pre><code>tell application "Foo"
        beep
    end tell
    </code></pre>

�@�ӵ{���X�϶��|�@�������S���Y�ƪ����@��]�άO��󵲧��^�C

�b�{���X�϶��̭��A `&` �B `<` �M `>` �|�۰��ন HTML ����A�o�˪��覡���A�D�`�e���ϥ� Markdown ���J�d�ҥΪ� HTML ��l�X�A�u�ݭn�ƻs�K�W�A�A�[�W�Y�ƴN�i�H�F�A�ѤU�� Markdown ���|���A�B�z�A�Ҧp�G

        <div class="footer">
            &copy; 2004 Foo Corporation
        </div>

�|�Q�ഫ���G

    <pre><code>&lt;div class="footer"&gt;
        &amp;copy; 2004 Foo Corporation
    &lt;/div&gt;
    </code></pre>

�{���X�϶����A�@�몺 Markdown �y�k���|�Q�ഫ�A���O�P���K�u�O�P���A�o��ܧA�i�H�ܮe���a�H Markdown �y�k���g Markdown �y�k���������C

<h3 id="hr">���j�u</h3>

�A�i�H�b�@�椤�ΤT�өΥH�W���P���B��B���u�ӫإߤ@�Ӥ��j�u�A�椺���঳��L�F��C�A�]�i�H�b�P���������J�ťաC�U���C�ؼg�k���i�H�إߤ��j�u�G

    * * *

    ***

    *****

    - - -

    ---------------------------------------


* * *

<h2 id="span">�Ϭq����</h2>

<h3 id="link">�s��</h3>

Markdown �䴩��اΦ����s���y�k�G *�椺*�M*�Ѧ�*��اΦ��C

���ެO���@�ءA�s������r���O�� [��A��] �ӼаO�C

�n�إߤ@�Ӧ椺�Φ����s���A�u�n�b����A���᭱���W���۬A���ô��J���}�s���Y�i�A�p�G�A�ٷQ�n�[�W�s���� title ��r�A�u�n�b���}�᭱�A�����޸��� title ��r�]�_�ӧY�i�A�Ҧp�G

    This is [an example](http://example.com/ "Title") inline link.

    [This link](http://example.net/) has no title attribute.

�|���͡G

    <p>This is <a href="http://example.com/" title="Title">
    an example</a> inline link.</p>

    <p><a href="http://example.net/">This link</a> has no
    title attribute.</p>

�p�G�A�O�n�s����P�˥D�����귽�A�A�i�H�ϥά۹���|�G

    See my [About](/about/) page for details.   

�ѦҧΦ����s���ϥΥt�~�@�Ӥ�A�����b�s����r���A���᭱�A�Ӧb�ĤG�Ӥ�A���̭��n��J�ΥH���ѳs�������ҡG

    This is [an example][id] reference-style link.

�A�]�i�H��ܩʦa�b��Ӥ�A�������[�W�ťաG

    This is [an example] [id] reference-style link.

���ۡA�b��󪺥��N�B�A�A�i�H��o�Ӽ��Ҫ��s�����e�w�q�X�ӡG

    [id]: http://example.com/  "Optional Title Here"

�s���w�q���Φ����G

*   ��A���A�̭���J�s�������ѥμ���
*   ���ۤ@�ӫ_��
*   ���ۤ@�ӥH�W���ťթ� tab
*   ���۳s�������}
*   ��ܩʦa���� title ���e�A�i�H�γ�޸��B���޸��άO�A���]��

�U���o�T�سs�����w�q���O�ۦP�G

	[foo]: http://example.com/  "Optional Title Here"
	[foo]: http://example.com/  'Optional Title Here'
	[foo]: http://example.com/  (Optional Title Here)

**�Ъ`�N�G**���@�Ӥw�������D�O Markdown.pl 1.0.1 �|������޸��]�_�Ӫ��s�� title�C

�s�����}�]�i�H�Τ�A���]�_�ӡG

    [id]: <http://example.com/>  "Optional Title Here"

�A�]�i�H�� title �ݩʩ��U�@��A�]�i�H�[�@���Y�ơA���}�Ӫ����ܡA�o�˷|����n�ݡG

    [id]: http://example.com/longish/path/to/resource/here
        "Optional Title Here"

���}�w�q�u���b���ͳs�����ɭԥΨ�A�ä��|�����X�{�b��󤧤��C

�s�����Ѽ��ҥi�H���r���B�Ʀr�B�ťթM���I�Ÿ��A���O��*��*�Ϥ��j�p�g�A�]���U����ӳs���O�@�˪��G

	[link text][a]
	[link text][A]

*�w�]���s������*�\�����A�i�H�ٲ����w�s�����ҡA�o�ر��ΤU�A�s�����ҩM�s����r�|�����ۦP�A�n�ιw�]�s�����ҥu�n�b�s����r�᭱�[�W�@�ӪŪ���A���A�p�G�A�n�� "Google" �s���� google.com�A�A�i�H²�Ʀ��G

	[Google][]

�M��w�q�s�����e�G

	[Google]: http://google.com/

�ѩ�s����r�i��]�t�ťաA�ҥH�o��²�ƪ����Ҥ��]�i�H�]�t�h�Ӥ�r�G

	Visit [Daring Fireball][] for more information.

�M�ᱵ�۩w�q�s���G
	
	[Daring Fireball]: http://daringfireball.net/

�s�����w�q�i�H��b��󤤪�����@�Ӧa��A�ڤ�����n������b�s���X�{�q�����᭱�A�A�]�i�H�⥦��b���̫᭱�A�N���O���Ѥ@�ˡC

�U���O�@�ӰѦҦ��s�����d�ҡG

    I get 10 times more traffic from [Google] [1] than from
    [Yahoo] [2] or [MSN] [3].

      [1]: http://google.com/        "Google"
      [2]: http://search.yahoo.com/  "Yahoo Search"
      [3]: http://search.msn.com/    "MSN Search"

�p�G�令�γs���W�٪��覡�g�G

    I get 10 times more traffic from [Google][] than from
    [Yahoo][] or [MSN][].

      [google]: http://google.com/        "Google"
      [yahoo]:  http://search.yahoo.com/  "Yahoo Search"
      [msn]:    http://search.msn.com/    "MSN Search"

�W����ؼg�k���|���ͤU���� HTML�C

    <p>I get 10 times more traffic from <a href="http://google.com/"
    title="Google">Google</a> than from
    <a href="http://search.yahoo.com/" title="Yahoo Search">Yahoo</a>
    or <a href="http://search.msn.com/" title="MSN Search">MSN</a>.</p>

�U���O�Φ椺�Φ��g���P�ˤ@�q���e�� Markdown ���A���ѧ@��������ΡG

    I get 10 times more traffic from [Google](http://google.com/ "Google")
    than from [Yahoo](http://search.yahoo.com/ "Yahoo Search") or
    [MSN](http://search.msn.com/ "MSN Search").

�ѦҦ����s����꭫�I���b�󥦤���n�g�A�ӬO������nŪ�A����@�U�W�����d�ҡA�ϥΰѦҦ����峹�����u�� 81 �Ӧr���A���O�Φ椺�Φ����s���o�|�W�[�� 176 �Ӧr���A�p�G�O�ί� HTML �榡�Ӽg�A�|�� 234 �Ӧr���A�b HTML �榡���A���Ҥ��r�٭n�h�C

�ϥ� Markdown ���ѦҦ��s���A�i�H�����󹳬O�s�����̫Უ�ͪ����G�A���A�i�H��@�ǼаO��������T����q����r���~�A�A�N�i�H�W�[�s���Ӥ����峹���\Ū�Pı�Q���_�C

<h3 id="em">�j��</h3>

Markdown �ϥάP���]`*`�^�M���u�]`_`�^�@���аO�j�զr�����Ÿ��A�Q `*` �� `_` �]�򪺦r���|�Q�ন�� `<em>` ���ҥ]��A�Ψ�� `*` �� `_` �]�_�Ӫ��ܡA�h�|�Q�ন `<strong>`�A�Ҧp�G

    *single asterisks*

    _single underscores_

    **double asterisks**

    __double underscores__

�|�ন�G

    <em>single asterisks</em>

    <em>single underscores</em>

    <strong>double asterisks</strong>

    <strong>double underscores</strong>

�A�i�H�H�K�ΧA���w���˦��A�ߤ@������O�A�A�Τ���Ÿ��}�Ҽ��ҡA�N�n�Τ���Ÿ������C

�j�դ]�i�H�������b��r�����G

    un*frigging*believable

���O�p�G�A�� `*` �M `_` ���䳣���ťժ��ܡA���̴N�u�|�Q�����q���Ÿ��C

�p�G�n�b��r�e�᪽�����J���q���P���Ω��u�A�A�i�H�Τϱ׽u�G

    \*this text is surrounded by literal asterisks\*

<h3 id="code">�{���X</h3>

�p�G�n�аO�@�p�q�椺�{���X�A�A�i�H�ΤϤ޸��⥦�]�_�ӡ]`` ` ``�^�A�Ҧp�G

    Use the `printf()` function.

�|���͡G

    <p>Use the <code>printf()</code> function.</p>

�p�G�n�b�{���X�Ϭq�����J�Ϥ޸��A�A�i�H�Φh�ӤϤ޸��Ӷ}�ҩM�����{���X�Ϭq�G

    ``There is a literal backtick (`) here.``

�o�q�y�k�|���͡G

    <p><code>There is a literal backtick (`) here.</code></p>

�{���X�Ϭq���_�l�M�����ݳ��i�H��J�@�ӪťաA�_�l�ݫ᭱�@�ӡA�����ݫe���@�ӡA�o�˧A�N�i�H�b�Ϭq���@�}�l�N���J�Ϥ޸��G

	A single backtick in a code span: `` ` ``
	
	A backtick-delimited string in a code span: `` `foo` ``

�|���͡G

	<p>A single backtick in a code span: <code>`</code></p>
	
	<p>A backtick-delimited string in a code span: <code>`foo`</code></p>

�b�{���X�Ϭq���A`&` �M��A�����|�Q�ন HTML ����A�o�˷|����e�����J HTML ��l�X�AMarkdown �|��U���o�q�G

    Please don't use any `<blink>` tags.

�ର�G

    <p>Please don't use any <code>&lt;blink&gt;</code> tags.</p>

�A�]�i�H�o�˼g�G

    `&#8212;` is the decimal-encoded equivalent of `&mdash;`.

�H���͡G

    <p><code>&amp;#8212;</code> is the decimal-encoded
    equivalent of <code>&amp;mdash;</code>.</p>



<h3 id="img">�Ϥ�</h3>

�ܩ���a�A�n�b�¤�r���Τ��]�p�@�� �u�۵M�v���y�k�Ӵ��J�Ϥ��O���@�w���ת��C

Markdown �ϥΤ@�ةM�s���ܬۦ����y�k�ӼаO�Ϥ��A�P�ˤ]���\��ؼ˦��G *�椺*�M*�Ѧ�*�C

�椺�Ϥ����y�k�ݰ_�ӹ��O�G

    ![Alt text](/path/to/img.jpg)

    ![Alt text](/path/to/img.jpg "Optional title")

�Բӱԭz�p�U�G

*   �@����ĸ� `!`
*   ���ۤ@���A���A�̭���W�Ϥ������N��r
*   ���ۤ@�ﴶ�q�A���A�̭���W�Ϥ������}�A�̫��٥i�H�Τ޸��]��å[�W
    ��ܩʪ� 'title' ��r�C

�ѦҦ����Ϥ��y�k�h���o���o�ˡG

    ![Alt text][id]

�uid�v�O�Ϥ��ѦҪ��W�١A�Ϥ��ѦҪ��w�q�覡�h�M�s���ѦҤ@�ˡG

    [id]: url/to/image  "Optional title attribute"

��ثe����A Markdown �٨S����k���w�Ϥ����e���A�p�G�A�ݭn���ܡA�A�i�H�ϥδ��q�� `<img>` ���ҡC

* * *

<h2 id="misc">�䥦</h2>

<h3 id="autolink">�۰ʳs��</h3>

Markdown �䴩���²�u���۰ʳs���Φ��ӳB�z���}�M�q�l�l��H�c�A�u�n�O�Τ�A���]�_�ӡA Markdown �N�|�۰ʧ⥦�ন�s���A�s������r�N�M�s����m�@�ˡA�Ҧp�G

    <http://example.com/>
    
Markdown �|�ର�G

    <a href="http://example.com/">http://example.com/</a>

�۰ʪ��l��s���]�������A�u�O Markdown �|�����@�ӽs�X�ഫ���L�{�A���r�r���ন 16 �i��X�� HTML ����A�o�˪��榡�i�H�V�c�@�Ǥ��n���H�c�a�}���������H�A�Ҧp�G

    <address@example.com>

Markdown �|�ন�G

    <a href="&#x6D;&#x61;i&#x6C;&#x74;&#x6F;:&#x61;&#x64;&#x64;&#x72;&#x65;
    &#115;&#115;&#64;&#101;&#120;&#x61;&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;
    &#109;">&#x61;&#x64;&#x64;&#x72;&#x65;&#115;&#115;&#64;&#101;&#120;&#x61;
    &#109;&#x70;&#x6C;e&#x2E;&#99;&#111;&#109;</a>

�b�s�����̭��A�o�q�r��|�ܦ��@�ӥi�H�I�����uaddress@example.com�v�s���C

�]�o�ا@�k���M�i�H�V�c���֪������H�A���õL�k�����פU�ӡA���L�o�ˤ]�񤰻򳣤����n�ǡC�L�צp��A���}�A���H�c�רs�|�ިӼs�i�H�󪺡C�^

<h3 id="backslash">����r��</h3>

Markdown �i�H�Q�Τϱ׽u�Ӵ��J�@�Ǧb�y�k�����䥦�N�q���Ÿ��A�Ҧp�G�p�G�A�Q�n�άP���[�b��r���䪺�覡�Ӱ��X�j�ծĪG�]������ `<em>` ���ҡ^�A�A�i�H�b�P�����e���[�W�ϱ׽u�G

    \*literal asterisks\*

Markdown �䴩�b�U���o�ǲŸ��e���[�W�ϱ׽u�����U���J���q���Ÿ��G

    \   �ϱ׽u
    `   �Ϥ޸�
    *   �P��
    _   ���u
    {}  �j�A��
    []  ��A��
    ()  �A��
    #   ���r��
	+	�[��
	-	�
    .   �^��y�I
    !   ��ĸ�

<h2 id="acknowledgement">�P��</h2>

�P�� [leafy7382][] ��U½Ķ�A[hlb][]�B[Randylien][] ������Z�A[ethantw][] ��[�~�r�зǮ榡?CSS Reset][]�A [WM][] �^����r���~�C

[leafy7382]:https://twitter.com/#!/leafy7382
[hlb]:http://iamhlb.com/
[Randylien]:http://twitter.com/randylien
[ethantw]:https://twitter.com/#!/ethantw
[�~�r�зǮ榡?CSS Reset]:http://ethantw.net/projects/han/
[WM]:http://kidwm.net/
