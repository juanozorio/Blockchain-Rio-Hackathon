import { Inter } from "next/font/google";
import "./globals.css";

import Menu from "@/components/Menu";
import Footer from "@/components/Footer";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({ children }) {
  return (
    <html lang="pt-br">
      <Menu className="flex justify-end max-w-xl" />
        <body className={inter.className}>{children}</body>
      <Footer />
    </html>
  );
}