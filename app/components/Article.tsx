import { Article } from "../types"

export default function ArticleComponent({ article }: { article: Article }) {
  return (
    <div className="flex flex-col gap-2">
        <a href={article.link} target="_blank" className="underline link-color">{article.title}</a>
    </div>
    )
}
