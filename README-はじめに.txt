カマスタ公式サイト・スマホ投稿対応版（準備済み／未公開）

【必要な無料サービス】
1. GitHub（コードと記事の保管）
2. Pages CMS（スマホで記事作成） https://app.pagescms.org/
3. Cloudflare Pages（サイト公開）

【初期設定】
1. このZIPを展開して、すべてのファイルをGitHubの新規リポジトリにアップロード（mainブランチ）。
2. GitHubの Settings > Actions > General > Workflow permissions で Read and write permissions を許可。
3. Pages CMSにGitHubでログインし、対象リポジトリへのアクセスを許可。
4. Pages CMSで「NEWS・お知らせ」「BLOG・コラム」を選び、タイトル、日付、本文、画像を入力。「公開する」をオンにして保存。
5. GitHub Actionsで記事一覧データが自動生成されます（通常数十秒〜数分）。
6. Cloudflare PagesをGitHubと連携して公開。ビルドコマンドは空欄、出力ディレクトリは / （またはリポジトリのルート）。GitHubの新しいコミットで自動更新されます。
7. 仮URLで検証後、既存ドメインを接続。Wix解約は最後。

【注意】
・Pages CMSのログインとGitHub権限の設定はご本人が行います。
・記事は公開するをオンにして保存後、GitHub Actionsが成功し、Cloudflareのデプロイが完了すると反映されます。
・公開をオフにすると記事一覧と記事詳細から非表示になりますが、GitHubに原稿は残ります。
・この仕組みはGitHubの非公開リポジトリでも利用可能ですが、無料枠の利用条件とGitHub Actionsの制限は各サービスで確認してください。
・記事の画像・本文は公開情報として扱い、個人情報や未公開の契約情報を載せないでください。
・応募ボタンはまだ公式LINEの本番URLに接続していません。
・会社の現行サイトは変更していません。
