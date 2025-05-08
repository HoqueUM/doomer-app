"use client";
import { useState, useEffect } from 'react';
import { Article } from '../types';
import ArticleComponent from './Article';
import { Skeleton } from "@/components/ui/skeleton";

export default function TruncatedArticles(): JSX.Element {
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    fetch('/api/get_news')
      .then(res => res.json())
      .then((data: Article[]) => {
        setArticles(data);
        setLoading(false);
      })
      .catch((error: Error) => {
        console.error('Error fetching articles:', error);
        setLoading(false);
      });
  }, []);

  return (
    <section className="py-12">
      <div className="mb-8 text-center">
        {/* <h2 className="text-3xl font-bold tracking-tight mb-2">Latest News</h2>
        <p className="text-muted-foreground max-w-lg mx-auto">
          Stay updated with the latest articles and insights from around the web.
        </p> */}
      </div>
      
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[...Array(6)].map((_, i) => (
            <div key={i} className="space-y-2">
              <Skeleton className="h-6 w-3/4" />
              <Skeleton className="h-4 w-1/2" />
              <div className="pt-4">
                <Skeleton className="h-4 w-1/4 ml-auto" />
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {articles.length > 0 ? (
            articles.slice(0, 30).map((article: Article) => (
              <ArticleComponent key={article.id} article={article} />
            ))
          ) : (
            <div className="col-span-3 text-center py-12">
              <p className="text-muted-foreground">No articles found.</p>
            </div>
          )}
        </div>
      )}
    </section>
  );
}